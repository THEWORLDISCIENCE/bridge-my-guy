
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="BridgeGuard AI",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

st.markdown("""
<style>
#MainMenu,footer,header,[data-testid="stToolbar"],
[data-testid="stDecoration"],[data-testid="stStatusWidget"] {
    display:none!important;
}
.stApp,[data-testid="stAppViewContainer"],
[data-testid="stMain"],.main,.block-container {
    padding:0!important;
    margin:0!important;
    max-width:100%!important;
    background:#9acde9!important;
}
iframe {
    border:0!important;
    display:block;
}
</style>
""", unsafe_allow_html=True)

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width,initial-scale=1">

<script type="importmap">
{
  "imports": {
    "three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
  }
}
</script>

<style>
* {box-sizing:border-box}

html,body {
    margin:0;
    width:100%;
    height:100%;
    overflow:hidden;
    font-family:Arial, sans-serif;
    background:#8dc6e8;
    color:#effaff;
}

#world {
    position:fixed;
    inset:0;
}

#world canvas {
    width:100%;
    height:100%;
    display:block;
}

.glass {
    position:absolute;
    z-index:4;
    color:#effaff;
    background:linear-gradient(
        145deg,
        rgba(8,34,58,.82),
        rgba(8,49,75,.68)
    );
    border:1px solid rgba(153,221,255,.38);
    border-radius:12px;
    box-shadow:0 10px 30px rgba(0,25,50,.25);
    backdrop-filter:blur(15px);
    padding:12px;
}

#header {
    top:12px;
    left:14px;
    right:14px;
    height:65px;
    display:flex;
    align-items:center;
    justify-content:space-between;
    padding:10px 18px;
}

.logo {
    font-size:17px;
    font-weight:900;
    letter-spacing:1px;
}

.kicker {
    font-size:9px;
    color:#a9d9ef;
    letter-spacing:2px;
    margin-top:5px;
}

.headright {
    display:flex;
    gap:8px;
    align-items:center;
}

.tag {
    padding:8px 11px;
    border-radius:20px;
    background:#22557488;
    border:1px solid #9cddf544;
    font-size:9px;
    white-space:nowrap;
}

.green {color:#5df0b2}

#left {
    left:14px;
    top:91px;
    width:230px;
    max-height:calc(100vh - 220px);
    overflow:auto;
}

#right {
    right:14px;
    top:91px;
    width:270px;
    max-height:calc(100vh - 220px);
    overflow:auto;
}

.heading {
    font-size:10px;
    letter-spacing:1.5px;
    color:#a3e1fa;
    font-weight:900;
    margin-bottom:12px;
}

.subheading {
    font-size:9px;
    letter-spacing:1px;
    color:#87cce9;
    margin:14px 0 8px;
    padding-top:10px;
    border-top:1px solid #ffffff22;
}

label {
    display:flex;
    justify-content:space-between;
    font-size:10px;
    color:#c8e0ee;
    margin:9px 0 5px;
}

output {
    color:white;
    font-weight:bold;
}

input[type=range] {
    width:100%;
    accent-color:#41d9ef;
}

select {
    width:100%;
    padding:8px;
    background:#123b55;
    color:white;
    border:1px solid #5487a1;
    border-radius:6px;
    font-size:10px;
}

button {
    background:linear-gradient(120deg,#147f9e,#20b4c7);
    border:1px solid #60d9e9;
    color:white;
    border-radius:7px;
    padding:9px;
    font-size:9px;
    font-weight:bold;
    cursor:pointer;
}

button.secondary {
    background:#183f56;
    border-color:#47788e;
}

button:hover {filter:brightness(1.2)}

.buttons {
    display:flex;
    gap:7px;
    margin-top:9px;
}

.buttons button {flex:1}

.metricgrid {
    display:grid;
    grid-template-columns:1fr 1fr;
    gap:7px;
}

.metric {
    padding:10px;
    border:1px solid #a6ddf022;
    border-radius:8px;
    background:#35708933;
}

.metricname {
    font-size:8px;
    color:#a9d1e3;
    letter-spacing:.6px;
}

.metricvalue {
    font-size:19px;
    font-weight:900;
    margin-top:5px;
}

.unit {
    font-size:8px;
    color:#9bc4d8;
}

.sensor {
    display:flex;
    justify-content:space-between;
    padding:7px 0;
    border-bottom:1px solid #ffffff16;
    font-size:9px;
    color:#c5deeb;
}

.on {
    color:#5de9ae;
    font-weight:bold;
}

.off {
    color:#f2bd82;
    font-weight:bold;
}

.alert {
    padding:9px;
    border-radius:8px;
    font-size:9px;
    line-height:1.6;
    background:#185c594f;
    border:1px solid #52d7ae55;
    margin-top:8px;
}

.warning {
    background:#9b63344c;
    border-color:#ffbd7655;
}

#bottom {
    bottom:12px;
    left:14px;
    right:14px;
    min-height:100px;
    display:grid;
    grid-template-columns:1fr 1fr 1.5fr 1fr;
    gap:12px;
}

.bottomlabel {
    font-size:8px;
    color:#9dd6ed;
    letter-spacing:1.4px;
    margin-bottom:8px;
}

.big {
    font-size:20px;
    font-weight:900;
}

.muted {
    font-size:9px;
    color:#a9cbdc;
    margin-top:5px;
}

#chart {
    width:100%;
    height:50px;
}

#chart polyline {
    fill:none;
    stroke:#59e0ef;
    stroke-width:2;
}

#chart polygon {fill:#49cde522}

#hint {
    position:absolute;
    z-index:3;
    bottom:120px;
    right:300px;
    font-size:9px;
    color:#153c50;
    background:#e8f7f8aa;
    padding:7px 10px;
    border-radius:7px;
}

#disclaimer {
    position:absolute;
    z-index:3;
    bottom:120px;
    left:50%;
    transform:translateX(-50%);
    font-size:8px;
    color:#163c50;
    background:#eaf8f5aa;
    padding:6px 10px;
    border-radius:20px;
    white-space:nowrap;
}

#loading {
    position:absolute;
    inset:0;
    z-index:10;
    display:grid;
    place-content:center;
    text-align:center;
    color:#153a50;
    background:linear-gradient(#94cce9,#d5e9df);
    font-size:17px;
    font-weight:900;
}

#loading small {
    font-size:10px;
    font-weight:normal;
    margin-top:10px;
}

#toast {
    display:none;
    position:absolute;
    z-index:12;
    top:90px;
    left:50%;
    transform:translateX(-50%);
    background:#123b51;
    padding:9px 15px;
    border-radius:8px;
    font-size:10px;
}

@media(max-width:850px) {
    #left {width:215px;left:8px}
    #right {width:225px;right:8px}
    #bottom {
        left:8px;
        right:8px;
        grid-template-columns:1fr 1fr;
    }
}

@media(max-width:600px) {
    #left {
        top:85px;
        width:47%;
        max-height:48vh;
    }
    #right {
        top:85px;
        width:47%;
        max-height:48vh;
    }
    #bottom {
        max-height:25vh;
        overflow:auto;
    }
    .logo {font-size:11px}
    .tag {font-size:7px;padding:6px}
    #disclaimer,#hint {display:none}
}
</style>
</head>

<body>

<div id="world"></div>

<div id="loading">
INITIALIZING BRIDGEGUARD AI
<small>Building 3D suspension bridge and sensor network...</small>
</div>

<div id="toast"></div>

<!-- HEADER -->
<div id="header" class="glass">
    <div>
        <div class="logo">🌉 BRIDGEGUARD AI</div>
        <div class="kicker">
            INTELLIGENT BRIDGE MONITORING · DIGITAL TWIN
        </div>
    </div>

    <div class="headright">
        <div class="tag">
            <span class="green">●</span> SYSTEM ONLINE
        </div>
        <div class="tag" id="mode">LIVE MONITORING</div>
        <div class="tag" id="clock">00:00:00</div>
    </div>
</div>

<!-- LEFT PANEL -->
<div id="left" class="glass">

    <div class="heading">01 / SIMULATION CONTROL</div>

    <label>Vehicle weight <output id="weightV">18 t</output></label>
    <input id="weight" type="range" min="5" max="45" value="18">

    <label>Vehicle speed <output id="speedV">55 km/h</output></label>
    <input id="speed" type="range" min="10" max="110" value="55">

    <label>Traffic volume <output id="trafficV">65%</output></label>
    <input id="traffic" type="range" min="0" max="100" value="65">

    <div class="subheading">STRUCTURAL CHANGE SCENARIO</div>

    <label>Stiffness change <output id="stiffV">0%</output></label>
    <input id="stiff" type="range" min="0" max="30" value="0">

    <label>Local change signal <output id="localV">0%</output></label>
    <input id="local" type="range" min="0" max="100" value="0">

    <label>Test location</label>
    <select id="location">
        <option>Midspan</option>
        <option>North tower</option>
        <option>South tower</option>
        <option>Deck joint</option>
        <option>Cable zone</option>
    </select>

    <div class="subheading">MONITORING CONFIGURATION</div>

    <select id="monitor">
        <option value="adaptive">Adaptive sensor attention</option>
        <option value="primary">Primary sensors only</option>
        <option value="all">All sensors active</option>
    </select>

    <div class="buttons">
        <button id="run">Ⅱ PAUSE</button>
        <button id="reset" class="secondary">↺ RESET</button>
    </div>

    <div class="buttons">
        <button id="vehicle">＋ VEHICLE</button>
        <button id="camera" class="secondary">CAMERA RESET</button>
    </div>

</div>

<!-- RIGHT PANEL -->
<div id="right" class="glass">

    <div class="heading">02 / LIVE STRUCTURAL TELEMETRY</div>

    <div class="metricgrid">

        <div class="metric">
            <div class="metricname">DECK DEFLECTION</div>
            <div class="metricvalue" id="deflection">2.40</div>
            <div class="unit">mm · simulated</div>
        </div>

        <div class="metric">
            <div class="metricname">STRAIN PROXY</div>
            <div class="metricvalue" id="strain">118</div>
            <div class="unit">με · simulated</div>
        </div>

        <div class="metric">
            <div class="metricname">VIBRATION</div>
            <div class="metricvalue" id="vibration">0.12</div>
            <div class="unit">g · simulated</div>
        </div>

        <div class="metric">
            <div class="metricname">TEMPERATURE</div>
            <div class="metricvalue" id="temperature">27.0</div>
            <div class="unit">°C · simulated</div>
        </div>

    </div>

    <div class="subheading">03 / SENSOR NETWORK</div>

    <div class="sensor"><span>Temperature</span><b class="on">ACTIVE</b></div>
    <div class="sensor"><span>Vibration</span><b class="on">ACTIVE</b></div>
    <div class="sensor"><span>Strain</span><b class="on">ACTIVE</b></div>
    <div class="sensor"><span>Humidity</span><b class="on">ACTIVE</b></div>
    <div class="sensor"><span>Water level</span><b class="on">ACTIVE</b></div>
    <div class="sensor"><span>Displacement</span><b class="on">ACTIVE</b></div>
    <div class="sensor"><span>Wind speed</span><b class="on">ACTIVE</b></div>
    <div class="sensor"><span>Pressure</span><b class="on">ACTIVE</b></div>

    <div class="subheading">04 / EVENT ANALYSIS</div>

    <div class="metricgrid">

        <div class="metric">
            <div class="metricname">BASELINE DEVIATION</div>
            <div class="metricvalue" id="deviation">0.0%</div>
        </div>

        <div class="metric">
            <div class="metricname">PERSISTENCE</div>
            <div class="metricvalue" id="persistence">LOW</div>
        </div>

    </div>

    <div id="alert" class="alert">
        Normal simulated operating pattern.
        Primary monitoring active.
    </div>

    <div class="subheading">05 / ADDITIONAL READINGS</div>

    <div class="sensor">
        <span>Tilt estimate</span>
        <b id="tilt">0.02°</b>
    </div>

    <div class="sensor">
        <span>Humidity</span>
        <b>68%</b>
    </div>

    <div class="sensor">
        <span>Crack-width proxy</span>
        <b id="crack">0.00 mm</b>
    </div>

    <div class="sensor">
        <span>Joint displacement</span>
        <b id="joint">0.30 mm</b>
    </div>

</div>

<div id="hint">
    DRAG TO ROTATE · SCROLL TO ZOOM
</div>

<div id="disclaimer">
    EDUCATIONAL SIMULATION · NOT A REAL BRIDGE SAFETY SYSTEM
</div>

<!-- BOTTOM DASHBOARD -->
<div id="bottom" class="glass">

    <div>
        <div class="bottomlabel">TRAFFIC / LOAD</div>
        <div class="big" id="trafficBig">65%</div>
        <div class="muted">Relative traffic volume</div>
        <div class="muted" id="count">Vehicles: 1</div>
    </div>

    <div>
        <div class="bottomlabel">STRUCTURAL RESPONSE</div>
        <div class="big" id="response">NORMAL</div>
        <div class="muted" id="responseNote">
            Within simulated baseline
        </div>
    </div>

    <div>
        <div class="bottomlabel">RESPONSE HISTORY</div>
        <svg id="chart" viewBox="0 0 400 55" preserveAspectRatio="none">
            <polygon id="fill" points="0,52 400,52"/>
            <polyline id="line" points="0,35 400,35"/>
        </svg>
        <div class="muted">Recent simulated measurements</div>
    </div>

    <div>
        <div class="bottomlabel">SYSTEM ACTIONS</div>
        <div class="buttons">
            <button id="export">EXPORT CSV</button>
            <button id="sensors" class="secondary">HIDE SENSORS</button>
        </div>
        <div class="muted" id="exportStatus">Live data collection</div>
    </div>

</div>

<script type="module">

import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import {Sky} from 'three/addons/objects/Sky.js';

// ======================================
// THREE.JS ENVIRONMENT
// ======================================

const root = document.getElementById('world');

const scene = new THREE.Scene();
scene.background = new THREE.Color(0x92c9ed);
scene.fog = new THREE.Fog(0x92c9ed, 500, 1700);

const camera = new THREE.PerspectiveCamera(
    43,
    innerWidth / innerHeight,
    0.1,
    4000
);

camera.position.set(190, 95, 220);

const renderer = new THREE.WebGLRenderer({
    antialias:true
});

renderer.setPixelRatio(Math.min(devicePixelRatio, 2));
renderer.setSize(innerWidth, innerHeight);
renderer.shadowMap.enabled = true;
renderer.shadowMap.type = THREE.PCFSoftShadowMap;
renderer.outputColorSpace = THREE.SRGBColorSpace;
renderer.toneMapping = THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure = 1.2;

root.appendChild(renderer.domElement);

const controls = new OrbitControls(
    camera,
    renderer.domElement
);

controls.enableDamping = true;
controls.dampingFactor = 0.05;
controls.maxPolarAngle = Math.PI * 0.49;
controls.minDistance = 40;
controls.maxDistance = 700;
controls.target.set(0, 28, 0);

// ======================================
// LIGHTING AND SKY
// ======================================

scene.add(
    new THREE.HemisphereLight(
        0xdaf4ff,
        0x54725a,
        2.0
    )
);

const sunlight = new THREE.DirectionalLight(
    0xfff3dc,
    3.5
);

sunlight.position.set(-180, 260, 160);
sunlight.castShadow = true;
sunlight.shadow.mapSize.set(2048,2048);
sunlight.shadow.camera.left = -300;
sunlight.shadow.camera.right = 300;
sunlight.shadow.camera.top = 300;
sunlight.shadow.camera.bottom = -300;

scene.add(sunlight);

const sky = new Sky();
sky.scale.setScalar(4500);

sky.material.uniforms.turbidity.value = 7;
sky.material.uniforms.rayleigh.value = 2.4;
sky.material.uniforms.mieCoefficient.value = 0.004;
sky.material.uniforms.mieDirectionalG.value = 0.8;

sky.material.uniforms.sunPosition.value
    .copy(sunlight.position)
    .normalize();

scene.add(sky);

// ======================================
// WATER
// ======================================

const waterMaterial = new THREE.MeshStandardMaterial({
    color:0x167ca6,
    roughness:0.24,
    metalness:0.25
});

const water = new THREE.Mesh(
    new THREE.PlaneGeometry(4000,4000),
    waterMaterial
);

water.rotation.x = -Math.PI/2;
water.position.y = -8;
water.receiveShadow = true;

scene.add(water);

// ======================================
// DISTANT LAND
// ======================================

const landMaterial = new THREE.MeshStandardMaterial({
    color:0x557c43,
    roughness:1
});

for(let i=0;i<28;i++){

    const hill = new THREE.Mesh(
        new THREE.SphereGeometry(1,24,16),
        landMaterial
    );

    hill.scale.set(
        45 + Math.random()*65,
        8 + Math.random()*8,
        28
    );

    hill.position.set(
        -550 + i*42,
        -4,
        i%2===0 ? -210 : 220
    );

    scene.add(hill);
}

// ======================================
// CLOUDS
// ======================================

const cloudMaterial = new THREE.MeshStandardMaterial({
    color:0xffffff,
    roughness:1,
    transparent:true,
    opacity:0.88
});

for(let i=0;i<42;i++){

    const cloud = new THREE.Group();

    const pieces = 4 + Math.floor(Math.random()*5);

    for(let j=0;j<pieces;j++){

        const puff = new THREE.Mesh(
            new THREE.SphereGeometry(
                1,
                16,
                12
            ),
            cloudMaterial
        );

        puff.scale.set(
            8 + Math.random()*13,
            5 + Math.random()*7,
            7 + Math.random()*10
        );

        puff.position.set(
            j*9,
            Math.random()*3,
            Math.random()*5
        );

        cloud.add(puff);
    }

    cloud.position.set(
        -350 + Math.random()*700,
        95 + Math.random()*100,
        -300 - Math.random()*180
    );

    scene.add(cloud);
}

// ======================================
// BRIDGE MATERIALS
// ======================================

const bridge = new THREE.Group();
scene.add(bridge);

const sensorGroup = new THREE.Group();
scene.add(sensorGroup);

const vehicleGroup = new THREE.Group();
scene.add(vehicleGroup);

const steel = new THREE.MeshStandardMaterial({
    color:0x879ba9,
    metalness:0.7,
    roughness:0.3
});

const darkSteel = new THREE.MeshStandardMaterial({
    color:0x455d70,
    metalness:0.65,
    roughness:0.35
});

const cableMaterial = new THREE.MeshStandardMaterial({
    color:0xd5e1e7,
    metalness:0.8,
    roughness:0.25
});

const deckMaterial = new THREE.MeshStandardMaterial({
    color:0x343e47,
    roughness:0.8
});

const concrete = new THREE.MeshStandardMaterial({
    color:0xc6cbd0,
    roughness:0.8
});

const roadLineMaterial = new THREE.MeshStandardMaterial({
    color:0xf1e7bd
});

// ======================================
// GEOMETRY HELPERS
// ======================================

function box(parent,x,y,z,sx,sy,sz,material){

    const mesh = new THREE.Mesh(
        new THREE.BoxGeometry(sx,sy,sz),
        material
    );

    mesh.position.set(x,y,z);
    mesh.castShadow = true;
    mesh.receiveShadow = true;

    parent.add(mesh);

    return mesh;
}

function beam(parent,a,b,radius,material){

    const direction = new THREE.Vector3().subVectors(b,a);

    const mesh = new THREE.Mesh(
        new THREE.CylinderGeometry(
            radius,
            radius,
            direction.length(),
            10
        ),
        material
    );

    mesh.position.copy(a).add(b).multiplyScalar(0.5);

    mesh.quaternion.setFromUnitVectors(
        new THREE.Vector3(0,1,0),
        direction.normalize()
    );

    mesh.castShadow = true;

    parent.add(mesh);

    return mesh;
}

// ======================================
// SUSPENSION BRIDGE
// ======================================

const L = 310;
const W = 25;
const deckY = 35;
const towerHeight = 95;

const leftTower = -70;
const rightTower = 70;

// Main road deck
box(
    bridge,
    0,
    deckY,
    0,
    L,
    3,
    W,
    deckMaterial
);

// Structural underside
box(
    bridge,
    0,
    deckY-2,
    0,
    L,
    1.2,
    W+2,
    steel
);

// Road lane markings
for(let z of [-6,0,6]){

    box(
        bridge,
        0,
        deckY+1.55,
        z,
        L,
        0.07,
        0.22,
        roadLineMaterial
    );
}

// Deck edges and guardrails
for(let z of [-W/2,W/2]){

    box(
        bridge,
        0,
        deckY+3,
        z,
        L,
        0.5,
        0.6,
        steel
    );

    box(
        bridge,
        0,
        deckY+5,
        z,
        L,
        0.25,
        0.25,
        cableMaterial
    );

    for(let x=-L/2;x<=L/2;x+=9){

        box(
            bridge,
            x,
            deckY+4,
            z,
            0.25,
            2,
            0.25,
            steel
        );
    }
}

// Suspension towers
for(const x of [leftTower,rightTower]){

    // Tower legs
    for(const z of [-8,8]){

        box(
            bridge,
            x,
            deckY+towerHeight/2,
            z,
            4,
            towerHeight,
            4,
            concrete
        );
    }

    // Tower portal crossbeam
    box(
        bridge,
        x,
        deckY+towerHeight,
        0,
        5,
        4,
        19,
        concrete
    );

    // Lower crossbeam
    box(
        bridge,
        x,
        deckY+30,
        0,
        4,
        3,
        18,
        steel
    );
}

// ======================================
// MAIN SUSPENSION CABLES
// ======================================

function cableHeight(x){

    const t = Math.abs(x)/155;

    return deckY + towerHeight - 7 - 72*(t*t);
}

for(const z of [-9,9]){

    const points = [];

    for(let i=0;i<=150;i++){

        const x = -155 + (310*i/150);

        points.push(
            new THREE.Vector3(
                x,
                cableHeight(x),
                z
            )
        );
    }

    const curve = new THREE.CatmullRomCurve3(points);

    const tube = new THREE.Mesh(
        new THREE.TubeGeometry(
            curve,
            220,
            0.42,
            8,
            false
        ),
        cableMaterial
    );

    bridge.add(tube);

    // Vertical suspension hangers
    for(let x=-145;x<=145;x+=6){

        const top = cableHeight(x);

        beam(
            bridge,
            new THREE.Vector3(x,deckY+2,z),
            new THREE.Vector3(x,top,z),
            0.13,
            cableMaterial
        );
    }
}

// ======================================
// ADDITIONAL BRIDGE BRACING
// ======================================

for(let x=-65;x<=65;x+=9){

    beam(
        bridge,
        new THREE.Vector3(x-4,deckY-2,-11),
        new THREE.Vector3(x+4,deckY-2,11),
        0.35,
        darkSteel
    );

    beam(
        bridge,
        new THREE.Vector3(x-4,deckY-2,11),
        new THREE.Vector3(x+4,deckY-2,-11),
        0.35,
        darkSteel
    );
}

// ======================================
// BRIDGE PIERS
// ======================================

for(const x of [-145,-110,110,145]){

    const pier = new THREE.Mesh(
        new THREE.CylinderGeometry(
            3.5,
            5,
            27,
            20
        ),
        concrete
    );

    pier.position.set(x,deckY/2-5,0);
    pier.castShadow = true;

    bridge.add(pier);

    const base = new THREE.Mesh(
        new THREE.CylinderGeometry(
            6,
            6,
            3,
            24
        ),
        concrete
    );

    base.position.set(x,-6,0);

    bridge.add(base);
}

// ======================================
// SENSOR NETWORK
// ======================================

const sensorColors = [
    0xff9f43,
    0x00d9ff,
    0x39e75f,
    0xe056fd,
    0xffd32a,
    0xff4757,
    0x70a1ff,
    0xffffff
];

const sensorNames = [
    "Temperature",
    "Vibration",
    "Strain",
    "Humidity",
    "Water Level",
    "Displacement",
    "Wind Speed",
    "Pressure"
];

function addSensor(x,y,z,color,size=1.2){

    const sphere = new THREE.Mesh(
        new THREE.SphereGeometry(size,16,16),
        new THREE.MeshStandardMaterial({
            color:color,
            emissive:color,
            emissiveIntensity:1.5
        })
    );

    sphere.position.set(x,y,z);
    sensorGroup.add(sphere);

    const halo = new THREE.Mesh(
        new THREE.SphereGeometry(size*2.2,12,12),
        new THREE.MeshBasicMaterial({
            color:color,
            transparent:true,
            opacity:0.13
        })
    );

    halo.position.copy(sphere.position);
    sensorGroup.add(halo);
}

// Initial sensor positions
for(let i=0;i<sensorNames.length;i++){

    addSensor(
        -130+i*37,
        deckY+3,
        13,
        sensorColors[i]
    );
}

for(let i=0;i<20;i++){

    addSensor(
        -140+i*14,
        deckY+3,
        -13,
        0x36cfff,
        0.8
    );
}

// ======================================
// VEHICLES
// ======================================

let vehicles = [];

function addVehicle(){

    const car = new THREE.Group();

    const body = new THREE.Mesh(
        new THREE.BoxGeometry(9,3,4.5),
        new THREE.MeshStandardMaterial({
            color:0xe6ecef,
            metalness:0.35,
            roughness:0.35
        })
    );

    body.position.y = 2.7;
    car.add(body);

    const cabin = new THREE.Mesh(
        new THREE.BoxGeometry(4,2.5,4),
        new THREE.MeshStandardMaterial({
            color:0x75a9c4,
            metalness:0.4,
            roughness:0.2
        })
    );

    cabin.position.set(-1.5,5.2,0);
    car.add(cabin);

    const wheelMaterial = new THREE.MeshStandardMaterial({
        color:0x151c22
    });

    for(const x of [-3,3]){
        for(const z of [-2.1,2.1]){

            const wheel = new THREE.Mesh(
                new THREE.CylinderGeometry(1,1,0.5,16),
                wheelMaterial
            );

            wheel.rotation.x = Math.PI/2;
            wheel.position.set(x,1.2,z);

            car.add(wheel);
        }
    }

    vehicleGroup.add(car);

    vehicles.push({
        mesh:car,
        position:Math.random()*0.8
    });
}

addVehicle();

// ======================================
// INTERFACE HELPERS
// ======================================

function put(id,value){

    document.getElementById(id).textContent = value;
}

function value(id){

    return Number(
        document.getElementById(id).value
    );
}

function toast(message){

    const element = document.getElementById('toast');

    element.textContent = message;
    element.style.display = 'block';

    setTimeout(()=>{
        element.style.display = 'none';
    },2000);
}

// ======================================
// CONTROL LABELS
// ======================================

function updateLabels(){

    put('weightV',value('weight')+' t');
    put('speedV',value('speed')+' km/h');
    put('trafficV',value('traffic')+'%');
    put('stiffV',value('stiff')+'%');
    put('localV',value('local')+'%');

    put('trafficBig',value('traffic')+'%');
}

[
    'weight',
    'speed',
    'traffic',
    'stiff',
    'local'
].forEach(id=>{

    document.getElementById(id).addEventListener(
        'input',
        updateLabels
    );
});

updateLabels();

// ======================================
// SIMULATION
// ======================================

let running = true;
let elapsed = 0;
let history = [];
let records = [];

function drawHistory(number){

    history.push(number);

    if(history.length>60){
        history.shift();
    }

    const points = history.map((v,i)=>{

        const x = i/(Math.max(1,history.length-1))*400;
        const y = 49-Math.min(v/40,1)*43;

        return x+','+y;
    }).join(' ');

    document.getElementById('line')
        .setAttribute('points',points);

    document.getElementById('fill')
        .setAttribute(
            'points',
            '0,52 '+points+' 400,52'
        );
}

function simulate(){

    const weight = value('weight')/45;
    const speed = value('speed')/110;
    const traffic = value('traffic')/100;

    const change =
        value('stiff')/30*0.75+
        value('local')/100*0.55;

    const load = weight*speed*traffic;

    const deviation = change*100+load*3;

    const deflection =
        0.7+load*4.4+change*5.2;

    const strain =
        72+load*110+change*180;

    const vibration =
        0.03+load*0.34+change*0.2;

    put('deflection',deflection.toFixed(2));
    put('strain',strain.toFixed(0));
    put('vibration',vibration.toFixed(2));

    put(
        'temperature',
        (27+Math.sin(elapsed/25)*1.5).toFixed(1)
    );

    put('deviation',deviation.toFixed(1)+'%');

    put(
        'persistence',
        change>0.3?'ELEVATED':
        change>0.08?'MODERATE':'LOW'
    );

    put('tilt',(0.02+change*0.6).toFixed(2)+'°');
    put('crack',(change*0.28).toFixed(2)+' mm');
    put('joint',(0.3+change*1.4).toFixed(2)+' mm');

    const alert = document.getElementById('alert');

    if(change>0.3){

        alert.className='alert warning';

        alert.textContent =
            'Persistent simulated change detected. Additional monitoring recommended.';

        put('response','CHANGE');
        put('responseNote','Simulated response differs from baseline');

    }else if(load>0.4){

        alert.className='alert';

        alert.textContent =
            'Elevated temporary traffic-load response detected.';

        put('response','LOAD');
        put('responseNote','Temporary load response in simulation');

    }else{

        alert.className='alert';

        alert.textContent =
            'Normal simulated operating pattern. Monitoring active.';

        put('response','NORMAL');
        put('responseNote','Within simulated baseline');
    }

    const mode = document.getElementById('monitor').value;

    put(
        'mode',
        mode==='all'?'ALL SENSORS ACTIVE':
        mode==='adaptive'?'ADAPTIVE MONITORING':
        'PRIMARY MONITORING'
    );

    drawHistory(deflection);

    records.push({
        time:elapsed.toFixed(1),
        weight:value('weight'),
        speed:value('speed'),
        traffic:value('traffic'),
        deflection:deflection.toFixed(3),
        strain:strain.toFixed(2),
        vibration:vibration.toFixed(3),
        temperature:(27+Math.sin(elapsed/25)*1.5).toFixed(2),
        deviation:deviation.toFixed(2)
    });

    if(records.length>2000){
        records.shift();
    }
}

// ======================================
// BUTTONS
// ======================================

document.getElementById('run').onclick=()=>{

    running=!running;

    put(
        'run',
        running?'Ⅱ PAUSE':'▶ RUN'
    );

    toast(
        running?'Simulation resumed':'Simulation paused'
    );
};

document.getElementById('reset').onclick=()=>{

    elapsed=0;
    history=[];
    records=[];

    document.getElementById('stiff').value=0;
    document.getElementById('local').value=0;

    updateLabels();
    simulate();

    toast('Simulation reset');
};

document.getElementById('vehicle').onclick=()=>{

    addVehicle();

    put('count','Vehicles: '+vehicles.length);

    toast('Vehicle added');
};

document.getElementById('camera').onclick=()=>{

    camera.position.set(190,95,220);

    controls.target.set(0,28,0);

    controls.update();

    toast('Camera reset');
};

document.getElementById('sensors').onclick=()=>{

    sensorGroup.visible=!sensorGroup.visible;

    put(
        'sensors',
        sensorGroup.visible?'HIDE SENSORS':'SHOW SENSORS'
    );
};

// ======================================
// CSV EXPORT
// ======================================

document.getElementById('export').onclick=()=>{

    if(!records.length){

        toast('No readings available yet');

        return;
    }

    const keys=Object.keys(records[0]);

    const csv=[
        keys.join(','),
        ...records.map(row=>
            keys.map(key=>row[key]).join(',')
        )
    ].join('\n');

    const link=document.createElement('a');

    link.href=URL.createObjectURL(
        new Blob([csv],{type:'text/csv'})
    );

    link.download='BridgeGuard-monitoring-data.csv';

    link.click();

    put('exportStatus','CSV exported');

    toast('Monitoring data exported');
};

// ======================================
// ANIMATION
// ======================================

const clock = new THREE.Clock();

function animate(){

    requestAnimationFrame(animate);

    const dt=Math.min(clock.getDelta(),0.05);

    if(running){

        elapsed+=dt;

        vehicles.forEach(vehicle=>{

            vehicle.position+=dt*
                (value('speed')/110)*0.08;

            if(vehicle.position>1.1){
                vehicle.position=-0.1;
            }

            const x=(vehicle.position-0.5)*260;

            vehicle.mesh.position.set(
                x,
                deckY+1,
                0
            );
        });

        if(
            Math.floor(elapsed*2)!==
            Math.floor((elapsed-dt)*2)
        ){

            simulate();
        }
    }

    put(
        'clock',
        new Date(
            Math.floor(elapsed)*1000
        ).toISOString().slice(11,19)
    );

    controls.update();

    renderer.render(scene,camera);
}

simulate();

document.getElementById('count').textContent =
    'Vehicles: '+vehicles.length;

document.getElementById('loading').style.display='none';

animate();

// ======================================
// RESPONSIVE WINDOW
// ======================================

window.addEventListener('resize',()=>{

    camera.aspect=innerWidth/innerHeight;

    camera.updateProjectionMatrix();

    renderer.setSize(innerWidth,innerHeight);
});

</script>

</body>
</html>
"""

components.html(
    html,
    height=1050,
    scrolling=False
)
