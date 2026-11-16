
import streamlit as st
import streamlit.components.v1 as components
import base64
from pathlib import Path

st.set_page_config(
    page_title="BridgeGuard AI | Digital Twin",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Load optional realistic bridge model
MODEL_PATH = Path("assets/bridge.glb")
MODEL_DATA = ""

if MODEL_PATH.exists():
    MODEL_DATA = base64.b64encode(MODEL_PATH.read_bytes()).decode("utf-8")

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<style>
* { box-sizing:border-box; }
body {
    margin:0;
    background:#07111d;
    color:#eaf3ff;
    font-family:Arial,sans-serif;
    overflow:hidden;
}
#scene {
    position:fixed;
    inset:0;
    width:100%;
    height:100%;
}
#topbar {
    position:absolute;
    top:14px;
    left:18px;
    right:18px;
    height:64px;
    background:rgba(5,15,29,.88);
    border:1px solid #24435d;
    border-radius:12px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:0 20px;
    z-index:5;
    backdrop-filter:blur(12px);
}
.brand {
    font-size:21px;
    font-weight:800;
    letter-spacing:2px;
}
.brand span { color:#24c7ff; }
.status {
    color:#55e6a5;
    font-size:12px;
    letter-spacing:1px;
}
.panel {
    position:absolute;
    top:94px;
    width:245px;
    background:rgba(5,16,30,.91);
    border:1px solid #23445f;
    border-radius:12px;
    padding:15px;
    z-index:4;
    backdrop-filter:blur(12px);
    box-shadow:0 10px 35px #0006;
}
#left { left:18px; }
#right { right:18px; width:260px; }
.panel h3 {
    margin:0 0 13px;
    color:#49cfff;
    font-size:13px;
    letter-spacing:1.5px;
}
label {
    display:block;
    font-size:11px;
    color:#9fb7ca;
    margin:12px 0 5px;
}
select,button {
    width:100%;
    padding:10px;
    border-radius:6px;
    border:1px solid #31536e;
    background:#10263b;
    color:white;
    font-size:12px;
}
button {
    cursor:pointer;
    margin-top:7px;
    font-weight:bold;
}
button:hover { background:#17466a; }
.primary {
    background:#087eb4;
    border-color:#20bfff;
}
.metric {
    border-bottom:1px solid #234057;
    padding:9px 0;
}
.metric small {
    color:#8fa9bf;
    font-size:10px;
    letter-spacing:1px;
}
.metric strong {
    display:block;
    font-size:22px;
    margin-top:3px;
}
.good { color:#4ce3a0; }
.warn { color:#ffca64; }
.bad { color:#ff657b; }
#bottom {
    position:absolute;
    bottom:14px;
    left:18px;
    right:18px;
    height:105px;
    background:rgba(5,16,30,.91);
    border:1px solid #23445f;
    border-radius:12px;
    z-index:4;
    padding:12px 16px;
    display:flex;
    gap:20px;
    align-items:center;
}
#chart {
    flex:1;
    height:75px;
    width:100%;
}
#alert {
    font-size:12px;
    color:#9fb7ca;
    line-height:1.6;
}
#sensorList {
    font-size:11px;
    color:#b5c9d9;
    line-height:1.8;
    max-height:130px;
    overflow:auto;
}
#hint {
    position:absolute;
    top:83px;
    left:50%;
    transform:translateX(-50%);
    z-index:3;
    font-size:11px;
    color:#c2d8e8;
    background:#071827bb;
    padding:7px 12px;
    border-radius:20px;
}
@media(max-width:800px) {
    .panel { width:190px; padding:10px; }
    #right { width:190px; }
    #left { left:8px; }
    #right { right:8px; }
    #topbar { left:8px; right:8px; }
    #bottom { left:8px; right:8px; }
}
</style>
</head>

<body>
<div id="scene"></div>

<div id="topbar">
    <div class="brand">🌉 BRIDGEGUARD <span>AI</span></div>
    <div class="status">● DIGITAL TWIN ONLINE</div>
</div>

<div id="hint">Drag to rotate · Scroll to zoom · Click bridge to place a sensor</div>

<div class="panel" id="left">
    <h3>ENGINEERING CONTROL</h3>

    <label>Sensor technology</label>
    <select id="sensorType">
        <option>Vibration</option>
        <option>Strain</option>
        <option>Temperature</option>
        <option>Humidity</option>
        <option>Water Level</option>
        <option>Displacement</option>
        <option>Wind Speed</option>
        <option>Pressure</option>
    </select>

    <button class="primary" onclick="placementMode()">＋ PLACE SENSOR</button>
    <button onclick="removeSensor()">REMOVE LAST SENSOR</button>
    <button onclick="toggleSensors()">SHOW / HIDE SENSORS</button>
    <button onclick="randomAnomaly()">⚠ SIMULATE ANOMALY</button>
    <button onclick="resetSimulation()">RESET SIMULATION</button>

    <label>Simulation speed</label>
    <select id="speed">
        <option value="1">Normal</option>
        <option value="2">2× Speed</option>
        <option value="4">4× Speed</option>
    </select>

    <label>INSTALLED SENSORS</label>
    <div id="sensorList">No sensors installed.</div>
</div>

<div class="panel" id="right">
    <h3>LIVE STRUCTURAL TELEMETRY</h3>

    <div class="metric">
        <small>STRUCTURAL HEALTH</small>
        <strong class="good" id="health">98.7%</strong>
    </div>

    <div class="metric">
        <small>VIBRATION</small>
        <strong id="vibration">0.42 mm/s</strong>
    </div>

    <div class="metric">
        <small>STRAIN</small>
        <strong id="strain">112 με</strong>
    </div>

    <div class="metric">
        <small>TEMPERATURE</small>
        <strong id="temperature">24.6 °C</strong>
    </div>

    <div class="metric">
        <small>WIND SPEED</small>
        <strong id="wind">12.4 km/h</strong>
    </div>

    <div class="metric">
        <small>RISK INDEX</small>
        <strong class="good" id="risk">LOW</strong>
    </div>

    <div class="metric">
        <small>AI ANALYSIS</small>
        <div id="analysis" style="font-size:11px;line-height:1.6;margin-top:6px">
            Monitoring initialized. No simulated abnormality detected.
        </div>
    </div>
</div>

<div id="bottom">
    <div style="min-width:190px">
        <div style="font-size:12px;color:#49cfff;font-weight:bold">
            LIVE VIBRATION HISTORY
        </div>
        <div id="alert">SYSTEM STATUS: NOMINAL<br>Waiting for sensor data...</div>
    </div>
    <canvas id="chart"></canvas>
</div>

<script type="module">
import * as THREE from
'https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js';

import { OrbitControls } from
'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/controls/OrbitControls.js';

import { GLTFLoader } from
'https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/loaders/GLTFLoader.js';

const MODEL_DATA = "__MODEL_DATA__";

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x9eb8ca);
scene.fog = new THREE.Fog(0x9eb8ca, 100, 260);

const camera = new THREE.PerspectiveCamera(
    42, window.innerWidth/window.innerHeight, 0.1, 1000
);
camera.position.set(75, 45, 95);

const renderer = new THREE.WebGLRenderer({
    antialias:true,
    alpha:false
});
renderer.setSize(window.innerWidth,window.innerHeight);
renderer.setPixelRatio(Math.min(window.devicePixelRatio,2));
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.15;

document.getElementById("scene").appendChild(renderer.domElement);

const controls = new OrbitControls(camera,renderer.domElement);
controls.enableDamping = true;
controls.dampingFactor = 0.055;
controls.target.set(0,9,0);
controls.maxPolarAngle = Math.PI/2.03;
controls.minDistance = 35;
controls.maxDistance = 190;

scene.add(new THREE.HemisphereLight(0xdceeff,0x344353,2.0));

const sun = new THREE.DirectionalLight(0xffedcf,3.2);
sun.position.set(-35,75,45);
sun.castShadow = true;
sun.shadow.mapSize.set(2048,2048);
sun.shadow.camera.left = -100;
sun.shadow.camera.right = 100;
sun.shadow.camera.top = 100;
sun.shadow.camera.bottom = -100;
scene.add(sun);

const fill = new THREE.DirectionalLight(0x83caff,1.1);
fill.position.set(50,30,-45);
scene.add(fill);

// Ground and horizon
const ground = new THREE.Mesh(
    new THREE.PlaneGeometry(1000,1000),
    new THREE.MeshStandardMaterial({
        color:0x71808b,
        roughness:0.95
    })
);
ground.rotation.x = -Math.PI/2;
ground.position.y = -1;
ground.receiveShadow = true;
scene.add(ground);

const grid = new THREE.GridHelper(500,80,0x59758a,0x71899b);
grid.position.y = -0.94;
grid.material.transparent = true;
grid.material.opacity = 0.16;
scene.add(grid);

const bridge = new THREE.Group();
scene.add(bridge);

const steel = new THREE.MeshStandardMaterial({
    color:0x667987,
    metalness:0.82,
    roughness:0.3
});
const darkSteel = new THREE.MeshStandardMaterial({
    color:0x283c4b,
    metalness:0.8,
    roughness:0.34
});
const concrete = new THREE.MeshStandardMaterial({
    color:0x929da4,
    metalness:0.12,
    roughness:0.83
});
const asphalt = new THREE.MeshStandardMaterial({
    color:0x252e36,
    roughness:0.9
});
const railMat = new THREE.MeshStandardMaterial({
    color:0x8799a5,
    metalness:0.7,
    roughness:0.3
});

function beam(a,b,r,material=steel,segments=10) {
    const start = new THREE.Vector3(...a);
    const end = new THREE.Vector3(...b);
    const direction = new THREE.Vector3().subVectors(end,start);
    const mesh = new THREE.Mesh(
        new THREE.CylinderGeometry(r,r,direction.length(),segments),
        material
    );
    mesh.position.copy(start).add(end).multiplyScalar(0.5);
    mesh.quaternion.setFromUnitVectors(
        new THREE.Vector3(0,1,0),
        direction.normalize()
    );
    mesh.castShadow = true;
    mesh.receiveShadow = true;
    bridge.add(mesh);
    return mesh;
}

function block(x,y,z,sx,sy,sz,material) {
    const mesh = new THREE.Mesh(
        new THREE.BoxGeometry(sx,sy,sz),
        material
    );
    mesh.position.set(x,y,z);
    mesh.castShadow = true;
    mesh.receiveShadow = true;
    bridge.add(mesh);
    return mesh;
}

function cable(points,r=0.16,material=darkSteel) {
    const curve = new THREE.CatmullRomCurve3(
        points.map(p=>new THREE.Vector3(...p))
    );
    const mesh = new THREE.Mesh(
        new THREE.TubeGeometry(curve,100,r,8,false),
        material
    );
    mesh.castShadow = true;
    bridge.add(mesh);
}

function buildFallbackBridge() {
    // Main road deck
    block(0,7,0,112,1.1,13,asphalt);

    // Deck edge girders and steel beams
    for (const z of [-6.2,6.2]) {
        block(0,6.3,z,112,0.8,0.6,darkSteel);
        block(0,7.75,z,112,0.25,0.25,railMat);
    }

    // Road lane markings
    const marking = new THREE.MeshStandardMaterial({
        color:0xe8e5c9,
        roughness:0.8
    });
    for (let x=-53;x<55;x+=8) {
        block(x,7.57,0,4,0.025,0.12,marking);
    }

    // Main suspension towers
    for (const x of [-22,22]) {
        for (const z of [-5.8,5.8]) {
            block(x,18,z,1.5,23,1.5,concrete);
            block(x,29.7,z,2.1,0.8,2.1,steel);
            block(x,7,z,2.2,1.2,2.2,darkSteel);
        }

        for (const z of [-5.8,5.8]) {
            beam([x,8,z],[x,28,z],0.24,darkSteel);
        }

        block(x,19,0,1.2,1.0,12,steel);
    }

    // Tower cross bracing
    for (const x of [-22,22]) {
        for (const z of [-5.8,5.8]) {
            beam([x-0.6,10,z],[x+0.6,26,z],0.18,steel);
            beam([x+0.6,10,z],[x-0.6,26,z],0.18,steel);
        }
    }

    // Main suspension cables on both sides
    for (const z of [-5.8,5.8]) {
        cable([
            [-56,23,z],[-42,29,z],[-22,31,z],
            [0,23,z],[22,31,z],[42,29,z],[56,23,z]
        ],0.23,darkSteel);

        // Vertical suspension hangers
        for (let x=-50;x<=50;x+=3.5) {
            const y = 23 + 8*Math.sin(
                (Math.abs(x)/56)*Math.PI/2
            );
            const towerAdjusted = Math.abs(x)<22 ?
                23 + 8*(1-Math.cos(Math.abs(x)/22*Math.PI/2)) :
                31 - 8*((Math.abs(x)-22)/34);

            beam([x,7.7,z],[x,towerAdjusted,z],0.065,steel,7);
        }
    }

    // Cross beams below deck
    for (let x=-54;x<=54;x+=3.5) {
        beam([x,6.2,-6],[x,6.2,6],0.18,darkSteel);
        beam([x,5.5,-5.8],[x,5.5,5.8],0.12,steel);
    }

    // Longitudinal under-deck truss elements
    for (const z of [-5.8,5.8]) {
        beam([-55,5.7,z],[55,5.7,z],0.18,darkSteel);

        for (let x=-53;x<54;x+=4) {
            beam([x,5.7,z],[x+4,6.2,z],0.11,steel);
            beam([x,6.2,z],[x+4,5.7,z],0.11,steel);
        }
    }

    // Cable anchor structures
    for (const x of [-57,57]) {
        for (const z of [-5.8,5.8]) {
            block(x,2,z,3,4,3,concrete);
            beam([x,3,z],[x,22,z],0.25,darkSteel);
        }
    }
}

let modelLoaded = false;

if (MODEL_DATA.length > 0) {
    try {
        const loader = new GLTFLoader();
        const dataUrl = "data:model/gltf-binary;base64," + MODEL_DATA;

        loader.load(dataUrl,(gltf)=>{
            const model = gltf.scene;
            const box = new THREE.Box3().setFromObject(model);
            const size = box.getSize(new THREE.Vector3());
            const center = box.getCenter(new THREE.Vector3());
            const maxDim = Math.max(size.x,size.y,size.z);
            const scale = 112 / maxDim;

            model.scale.setScalar(scale);
            model.position.sub(center.multiplyScalar(scale));
            model.traverse(obj=>{
                if(obj.isMesh) {
                    obj.castShadow = true;
                    obj.receiveShadow = true;
                }
            });
            bridge.add(model);
            modelLoaded = true;
        },undefined,()=>{
            buildFallbackBridge();
        });
    } catch(e) {
        buildFallbackBridge();
    }
} else {
    buildFallbackBridge();
}

// Sensor system
const sensorColors = {
    "Vibration":0x29d8ff,
    "Strain":0xffb52e,
    "Temperature":0xff684f,
    "Humidity":0x45a8ff,
    "Water Level":0x47d9c7,
    "Displacement":0xd17cff,
    "Wind Speed":0x9bff69,
    "Pressure":0xff6cbd
};

const sensors = [];
const sensorGroup = new THREE.Group();
scene.add(sensorGroup);

let placing = false;
let sensorsVisible = true;
let anomaly = false;
let tick = 0;
let vibrationHistory = Array(90).fill(0.4);

const raycaster = new THREE.Raycaster();
const pointer = new THREE.Vector2();

function placementMode() {
    placing = true;
    document.getElementById("alert").innerText =
        "PLACEMENT MODE ACTIVE: Click anywhere on the bridge.";
}

function updateSensorList() {
    const list = document.getElementById("sensorList");
    if (!sensors.length) {
        list.innerText = "No sensors installed.";
        return;
    }

    list.innerHTML = sensors.map((s,i)=>
        (i+1)+". "+s.type
    ).join("<br>");
}

function addSensor(point) {
    const type = document.getElementById("sensorType").value;
    const color = sensorColors[type];

    const marker = new THREE.Mesh(
        new THREE.SphereGeometry(0.55,20,20),
        new THREE.MeshStandardMaterial({
            color:color,
            emissive:color,
            emissiveIntensity:0.8,
            metalness:0.4,
            roughness:0.2
        })
    );
    marker.position.copy(point);
    marker.position.y += 0.65;
    marker.castShadow = true;

    const ring = new THREE.Mesh(
        new THREE.TorusGeometry(0.85,0.055,8,32),
        new THREE.MeshBasicMaterial({
            color:color,
            transparent:true,
            opacity:0.9
        })
    );
    ring.position.copy(marker.position);
    ring.rotation.x = Math.PI/2;

    sensorGroup.add(marker);
    sensorGroup.add(ring);

    sensors.push({
        type:type,
        marker:marker,
        ring:ring
    });

    updateSensorList();
    document.getElementById("alert").innerText =
        type.toUpperCase()+" SENSOR INSTALLED SUCCESSFULLY.";
}

renderer.domElement.addEventListener("click",(event)=>{
    if (!placing) return;

    const rect = renderer.domElement.getBoundingClientRect();
    pointer.x = ((event.clientX-rect.left)/rect.width)*2-1;
    pointer.y = -((event.clientY-rect.top)/rect.height)*2+1;

    raycaster.setFromCamera(pointer,camera);
    const hits = raycaster.intersectObjects(bridge.children,true);

    if (hits.length) {
        addSensor(hits[0].point);
        placing = false;
    }
});

function removeSensor() {
    const s = sensors.pop();
    if (!s) return;
    sensorGroup.remove(s.marker);
    sensorGroup.remove(s.ring);
    updateSensorList();
}

function toggleSensors() {
    sensorsVisible = !sensorsVisible;
    sensorGroup.visible = sensorsVisible;
}

function randomAnomaly() {
    anomaly = true;
    document.getElementById("alert").innerText =
        "WARNING: SIMULATED STRUCTURAL ANOMALY ACTIVATED.";
    document.getElementById("analysis").innerText =
        "An abnormal sensor pattern has been introduced into the educational simulation. Monitoring affected readings.";
}

function resetSimulation() {
    anomaly = false;
    placing = false;

    while (sensors.length) {
        const s = sensors.pop();
        sensorGroup.remove(s.marker);
        sensorGroup.remove(s.ring);
    }

    updateSensorList();
    document.getElementById("analysis").innerText =
        "Monitoring initialized. No simulated abnormality detected.";
    document.getElementById("alert").innerText =
        "SYSTEM STATUS: NOMINAL";
}

function updateMetrics() {
    const speed = Number(document.getElementById("speed").value);

    tick += 0.025*speed;

    let vib = 0.35 + Math.sin(tick)*0.12 +
              Math.random()*0.08;
    let strainValue = 110 + Math.sin(tick*0.7)*8;
    let temp = 24.5 + Math.sin(tick*0.15)*1.2;
    let wind = 12 + Math.sin(tick*0.4)*3;

    if (anomaly) {
        vib += 2.2 + Math.random()*1.3;
        strainValue += 75;
    }

    const risk = anomaly ? "HIGH" : "LOW";
    const health = anomaly ? 82.4 : 98.7;

    document.getElementById("vibration").innerText =
        vib.toFixed(2)+" mm/s";
    document.getElementById("strain").innerText =
        strainValue.toFixed(0)+" με";
    document.getElementById("temperature").innerText =
        temp.toFixed(1)+" °C";
    document.getElementById("wind").innerText =
        wind.toFixed(1)+" km/h";
    document.getElementById("health").innerText =
        health.toFixed(1)+"%";
    document.getElementById("risk").innerText = risk;

    document.getElementById("health").className =
        anomaly ? "warn" : "good";
    document.getElementById("risk").className =
        anomaly ? "bad" : "good";

    if (anomaly) {
        document.getElementById("analysis").innerText =
            "AI ALERT: Unusual vibration and strain patterns detected. Simulated inspection recommended.";
    } else {
        document.getElementById("analysis").innerText =
            "AI STATUS: Sensor readings are within the simulation's normal operating range.";
    }

    vibrationHistory.push(vib);
    if (vibrationHistory.length>90) vibrationHistory.shift();

    drawChart();
}

function drawChart() {
    const canvas = document.getElementById("chart");
    const ctx = canvas.getContext("2d");
    const w = canvas.width = canvas.clientWidth*devicePixelRatio;
    const h = canvas.height = canvas.clientHeight*devicePixelRatio;

    ctx.clearRect(0,0,w,h);

    ctx.strokeStyle = "#24445b";
    ctx.lineWidth = 1;
    for(let i=1;i<4;i++) {
        ctx.beginPath();
        ctx.moveTo(0,h*i/4);
        ctx.lineTo(w,h*i/4);
        ctx.stroke();
    }

    ctx.beginPath();
    vibrationHistory.forEach((v,i)=>{
        const x = i/(vibrationHistory.length-1)*w;
        const y = h-(v/4)*h;
        if(i===0) ctx.moveTo(x,y);
        else ctx.lineTo(x,y);
    });

    ctx.strokeStyle = anomaly ? "#ff667d" : "#36d6ff";
    ctx.lineWidth = 3*devicePixelRatio;
    ctx.stroke();
}

function animate() {
    requestAnimationFrame(animate);
    controls.update();

    sensorGroup.children.forEach((obj,i)=>{
        if(obj.geometry && obj.geometry.type==="TorusGeometry") {
            obj.rotation.z += 0.008;
        }
    });

    renderer.render(scene,camera);
}

animate();
setInterval(updateMetrics,1000);

window.addEventListener("resize",()=>{
    camera.aspect = window.innerWidth/window.innerHeight;
    camera.updateProjectionMatrix();
    renderer.setSize(window.innerWidth,window.innerHeight);
});

</script>
</body>
</html>
"""

html = html.replace("__MODEL_DATA__", MODEL_DATA)

components.html(
    html,
    height=1050,
    scrolling=False
)

