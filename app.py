
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="BridgeGuard AI | Digital Twin",
    page_icon="🌉",
    layout="wide",
    initial_sidebar_state="collapsed"
)

html = r"""
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<meta name="viewport" content="width=device-width, initial-scale=1.0">

<script type="importmap">
{
  "imports": {
    "three": "https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
    "three/addons/": "https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
  }
}
</script>

<style>
*{box-sizing:border-box}
body{
 margin:0;background:#07111f;color:#e8f1ff;
 font-family:Inter,Arial,sans-serif;overflow:hidden
}
#app{height:100vh;min-height:850px;position:relative;background:#07111f}
#scene{position:absolute;inset:0}
#scene canvas{display:block;width:100%;height:100%}
.topbar{
 position:absolute;top:0;left:0;right:0;height:66px;
 background:linear-gradient(90deg,rgba(5,15,29,.97),rgba(12,31,52,.88));
 border-bottom:1px solid #28415c;display:flex;align-items:center;
 justify-content:space-between;padding:0 24px;z-index:5
}
.brand{font-size:20px;font-weight:800;letter-spacing:1.5px}
.brand span{color:#42c9ff}
.subtitle{font-size:10px;color:#8da7c3;letter-spacing:2px;margin-top:4px}
.live{color:#55e5a5;font-size:11px;letter-spacing:1px}
.dot{display:inline-block;width:8px;height:8px;border-radius:50%;background:#45e6a0;margin-right:7px;box-shadow:0 0 12px #45e6a0}
.panel{
 background:linear-gradient(145deg,rgba(8,23,41,.94),rgba(12,32,53,.88));
 border:1px solid rgba(92,143,183,.3);border-radius:12px;
 box-shadow:0 12px 35px rgba(0,0,0,.25);backdrop-filter:blur(12px)
}
.left{
 position:absolute;top:84px;left:18px;width:245px;padding:16px;z-index:4
}
.right{
 position:absolute;top:84px;right:18px;width:270px;padding:16px;z-index:4
}
.bottom{
 position:absolute;left:280px;right:306px;bottom:16px;height:165px;
 padding:14px 18px;z-index:4
}
h3{font-size:11px;letter-spacing:1.7px;color:#86a8c8;margin:0 0 13px}
.section{border-bottom:1px solid #233d56;padding-bottom:14px;margin-bottom:14px}
.small{font-size:10px;color:#88a2bd}
button,select{
 background:#102b45;border:1px solid #315878;color:#eaf5ff;
 border-radius:6px;padding:9px 10px;font-size:11px;cursor:pointer
}
button:hover{background:#17476c;border-color:#4bc7ff}
button.primary{background:#087cae;border-color:#26b8f2}
button.danger{background:#48232d;border-color:#a54c5c}
button.active{background:#087cae;border-color:#42c9ff}
select{width:100%;margin:6px 0 8px}
.btnrow{display:flex;gap:7px;margin-top:8px}
.btnrow button{flex:1}
.metric{
 display:flex;justify-content:space-between;align-items:center;
 padding:9px 0;border-bottom:1px solid rgba(66,100,130,.25)
}
.metric:last-child{border:0}
.metric-name{font-size:11px;color:#a7bdd2}
.metric-value{font-size:16px;font-weight:700;font-variant-numeric:tabular-nums}
.unit{font-size:9px;color:#7894ae;margin-left:3px}
.good{color:#48e4a1}.warn{color:#ffc45c}.bad{color:#ff647c}
.status{
 padding:12px;border-radius:8px;background:rgba(27,91,72,.25);
 border:1px solid rgba(70,221,163,.3);margin-bottom:12px
}
.status.alert{background:rgba(130,46,56,.22);border-color:rgba(255,90,110,.5)}
.status strong{font-size:13px}
.status p{font-size:10px;color:#a5b9ca;margin:5px 0 0}
.sensor-list{max-height:115px;overflow:auto}
.sensor-item{font-size:10px;color:#b6cbe0;padding:5px 0;border-bottom:1px solid #203b53}
#chart{width:100%;height:95px}
.charthead{display:flex;justify-content:space-between;align-items:center}
#hint{
 position:absolute;left:50%;top:78px;transform:translateX(-50%);
 background:rgba(5,20,36,.9);border:1px solid #367ca2;
 padding:9px 15px;border-radius:7px;font-size:11px;z-index:6;
 display:none
}
#toast{
 position:absolute;bottom:195px;left:50%;transform:translateX(-50%);
 padding:9px 15px;background:#0d3852;border:1px solid #39b8e7;
 border-radius:8px;font-size:11px;display:none;z-index:8
}
#footer{
 position:absolute;bottom:7px;left:18px;font-size:9px;
 color:#7890a8;z-index:4
}
@media(max-width:850px){
 .left{width:190px;left:8px;top:76px;padding:10px}
 .right{width:205px;right:8px;top:76px;padding:10px}
 .bottom{left:8px;right:8px;bottom:10px;height:130px}
 .topbar{padding:0 12px}
 #footer{display:none}
}
</style>
</head>

<body>
<div id="app">
 <div id="scene"></div>

 <div class="topbar">
  <div>
   <div class="brand">BRIDGE<span>GUARD</span> AI</div>
   <div class="subtitle">INTELLIGENT INFRASTRUCTURE DIGITAL TWIN</div>
  </div>
  <div class="live"><span class="dot"></span>SIMULATION ONLINE</div>
 </div>

 <div id="hint">CLICK ON THE BRIDGE TO PLACE YOUR SENSOR</div>
 <div id="toast"></div>

 <div class="left panel">
  <h3>CONTROL CENTER</h3>
  <div class="section">
   <div class="small">SENSOR TYPE</div>
   <select id="sensorType">
    <option value="Temperature">Temperature</option>
    <option value="Vibration">Vibration</option>
    <option value="Strain">Strain</option>
    <option value="Humidity">Humidity</option>
    <option value="Water Level">Water Level</option>
    <option value="Displacement">Displacement</option>
    <option value="Wind Speed">Wind Speed</option>
    <option value="Pressure">Pressure</option>
   </select>
   <button class="primary" id="placeBtn" style="width:100%">＋ PLACE SENSOR</button>
   <div class="btnrow">
    <button id="cancelBtn">Cancel</button>
    <button id="removeBtn">Remove last</button>
   </div>
   <div class="btnrow">
    <button id="showBtn">Hide sensors</button>
    <button id="resetBtn">Reset</button>
   </div>
  </div>

  <div class="section">
   <h3>SIMULATION</h3>
   <div class="btnrow">
    <button class="primary" id="pauseBtn">Ⅱ Pause</button>
    <button id="anomalyBtn">⚠ Anomaly</button>
   </div>
   <div class="small" style="margin-top:9px">SIMULATION SPEED</div>
   <select id="speed">
    <option value="1">1× Normal</option>
    <option value="2">2× Fast</option>
    <option value="4">4× Very fast</option>
   </select>
  </div>

  <div>
   <h3>INSTALLED SENSORS <span id="sensorCount">0</span></h3>
   <div class="sensor-list" id="sensorList">
    <div class="small">No sensors placed yet.</div>
   </div>
  </div>
 </div>

 <div class="right panel">
  <h3>STRUCTURAL HEALTH MONITOR</h3>
  <div class="status" id="healthBox">
   <strong id="healthText" class="good">● NORMAL CONDITION</strong>
   <p id="healthDesc">All simulated parameters within normal range.</p>
  </div>
  <div class="small" style="margin-bottom:7px">LIVE TELEMETRY</div>
  <div id="metrics">
   <div class="metric"><span class="metric-name">Temperature</span><span class="metric-value" id="temperature">24.0<span class="unit">°C</span></span></div>
   <div class="metric"><span class="metric-name">Vibration</span><span class="metric-value" id="vibration">0.8<span class="unit">mm/s</span></span></div>
   <div class="metric"><span class="metric-name">Strain</span><span class="metric-value" id="strain">120<span class="unit">με</span></span></div>
   <div class="metric"><span class="metric-name">Humidity</span><span class="metric-value" id="humidity">58<span class="unit">%</span></span></div>
   <div class="metric"><span class="metric-name">Water Level</span><span class="metric-value" id="water">2.1<span class="unit">m</span></span></div>
   <div class="metric"><span class="metric-name">Displacement</span><span class="metric-value" id="displacement">1.2<span class="unit">mm</span></span></div>
   <div class="metric"><span class="metric-name">Wind Speed</span><span class="metric-value" id="wind">12<span class="unit">km/h</span></span></div>
   <div class="metric"><span class="metric-name">Pressure</span><span class="metric-value" id="pressure">101.3<span class="unit">kPa</span></span></div>
  </div>
  <div style="margin-top:13px">
   <h3>AI-STYLE ANALYSIS</h3>
   <div class="metric">
    <span class="metric-name">Illustrative risk score</span>
    <span class="metric-value" id="risk">08%</span>
   </div>
   <div class="metric">
    <span class="metric-name">Active alerts</span>
    <span class="metric-value" id="alerts">0</span>
   </div>
   <div class="small" id="aiText" style="line-height:1.5;margin-top:8px">
    Rule-based simulation is monitoring the displayed readings.
   </div>
  </div>
 </div>

 <div class="bottom panel">
  <div class="charthead">
   <h3>LIVE STRUCTURAL RESPONSE</h3>
   <div class="small">SIMULATED VIBRATION · mm/s</div>
  </div>
  <canvas id="chart"></canvas>
 </div>

 <div id="footer">
  EDUCATIONAL DIGITAL TWIN · SIMULATED DATA ONLY · NOT FOR REAL-WORLD STRUCTURAL SAFETY DECISIONS
 </div>
</div>

<script type="module">
import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';

const host=document.getElementById('scene');
const scene=new THREE.Scene();
scene.background=new THREE.Color(0x91a9bd);
scene.fog=new THREE.Fog(0x91a9bd,90,260);

const camera=new THREE.PerspectiveCamera(43,innerWidth/innerHeight,0.1,600);
camera.position.set(48,29,58);

const renderer=new THREE.WebGLRenderer({antialias:true,powerPreference:'high-performance'});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));
renderer.setSize(innerWidth,innerHeight);
renderer.shadowMap.enabled=true;
renderer.shadowMap.type=THREE.PCFSoftShadowMap;
renderer.outputColorSpace=THREE.SRGBColorSpace;
renderer.toneMapping=THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure=1.15;
host.appendChild(renderer.domElement);

const controls=new OrbitControls(camera,renderer.domElement);
controls.target.set(0,8,0);
controls.enableDamping=true;
controls.dampingFactor=.055;
controls.maxPolarAngle=Math.PI*.48;
controls.minDistance=18;
controls.maxDistance=125;

scene.add(new THREE.HemisphereLight(0xddeeff,0x465363,2.0));
const sun=new THREE.DirectionalLight(0xffe6c7,3.1);
sun.position.set(-35,65,35);
sun.castShadow=true;
sun.shadow.mapSize.set(2048,2048);
sun.shadow.camera.left=-90;
sun.shadow.camera.right=90;
sun.shadow.camera.top=90;
sun.shadow.camera.bottom=-90;
scene.add(sun);

const steel=new THREE.MeshStandardMaterial({color:0x526b80,metalness:.78,roughness:.3});
const darkSteel=new THREE.MeshStandardMaterial({color:0x263d50,metalness:.8,roughness:.32});
const concrete=new THREE.MeshStandardMaterial({color:0x9ba7ad,metalness:.12,roughness:.78});
const asphalt=new THREE.MeshStandardMaterial({color:0x252d35,metalness:.1,roughness:.92});
const laneMat=new THREE.MeshStandardMaterial({color:0xe8e6d9,roughness:.8});
const gold=new THREE.MeshStandardMaterial({color:0xd9b36e,metalness:.55,roughness:.35});
const groundMat=new THREE.MeshStandardMaterial({color:0x4c5b61,roughness:1});

const bridge=new THREE.Group();
scene.add(bridge);

function box(parent,w,h,d,x,y,z,mat){
 const m=new THREE.Mesh(new THREE.BoxGeometry(w,h,d),mat);
 m.position.set(x,y,z);m.castShadow=true;m.receiveShadow=true;
 parent.add(m);return m;
}
function beam(parent,a,b,r,mat,radial=8){
 const A=new THREE.Vector3(...a),B=new THREE.Vector3(...b);
 const dir=new THREE.Vector3().subVectors(B,A);
 const m=new THREE.Mesh(new THREE.CylinderGeometry(r,r,dir.length(),radial),mat);
 m.position.copy(A).add(B).multiplyScalar(.5);
 m.quaternion.setFromUnitVectors(new THREE.Vector3(0,1,0),dir.normalize());
 m.castShadow=true;m.receiveShadow=true;parent.add(m);return m;
}
function cable(parent,points,r,mat){
 const curve=new THREE.CatmullRomCurve3(points.map(p=>new THREE.Vector3(...p)));
 const mesh=new THREE.Mesh(new THREE.TubeGeometry(curve,100,r,8,false),mat);
 mesh.castShadow=true;parent.add(mesh);return mesh;
}

// Ground and distant atmospheric horizon
box(scene,420,.8,420,0,-3.2,0,groundMat);
const horizonMat=new THREE.MeshStandardMaterial({color:0x87979c,roughness:1});
for(let i=0;i<12;i++){
 const h=8+Math.random()*12;
 const m=new THREE.Mesh(new THREE.BoxGeometry(14+Math.random()*12,h,5),horizonMat);
 m.position.set(-85+i*16,h/2-2,-90-Math.random()*18);
 scene.add(m);
}

// Bridge deck: long, broad, elevated road surface
const deckY=8, length=112, width=13;
box(bridge,length,1.1,width,0,deckY,0,asphalt);
box(bridge,length,.35,width+.7,0,deckY-.65,0,darkSteel);

// Road markings
for(let x=-52;x<55;x+=7){
 box(bridge,3.1,.035,.13,x,deckY+.57,0,laneMat);
}
for(const z of [-5.6,5.6]){
 box(bridge,length,.12,.28,0,deckY+.62,z,laneMat);
}

// Deck edge girders and cross members
for(const z of [-6.3,6.3]){
 box(bridge,length,.65,.55,0,deckY-.2,z,darkSteel);
 for(let x=-54;x<=54;x+=4){
  box(bridge,.24,.5,width,x,deckY-.75,0,steel);
 }
}

// Guard rails and posts
for(const z of [-6.6,6.6]){
 for(let x=-55;x<=55;x+=2.2){
  beam(bridge,[x,deckY+.55,z],[x,deckY+1.6,z],.075,steel,8);
 }
 beam(bridge,[-56,deckY+1.6,z],[56,deckY+1.6,z],.12,steel,8);
 beam(bridge,[-56,deckY+1.25,z],[56,deckY+1.25,z],.07,darkSteel,8);
}

// Main suspension towers
const towerXs=[-22,22];
for(const x of towerXs){
 for(const z of [-4.5,4.5]){
  box(bridge,1.25,24,1.25,x,deckY+11.4,z,concrete);
  box(bridge,1.55,.65,1.55,x,deckY+23.6,z,gold);
 }
 // Portal crossbeam
 box(bridge,2,1.3,10,x,deckY+22.2,0,steel);
 box(bridge,1.4,1.0,10,x,deckY+11.2,0,steel);
 // X bracing on tower faces
 for(const z of [-4.6,4.6]){
  beam(bridge,[x,deckY+2,z],[x,deckY+10.8,z],.17,darkSteel);
  beam(bridge,[x,deckY+10.8,z],[x,deckY+2,z],.17,darkSteel);
 }
}

// Main suspension cables, two on each side
for(const z of [-4.5,4.5]){
 const points=[];
 for(let i=0;i<=80;i++){
  const x=-56+i*112/80;
  const sag=6.2*(1-(x/56)*(x/56));
  points.push([x,deckY+16.5-sag,z]);
 }
 cable(bridge,points,.24,darkSteel);
 // Vertical hangers
 for(let x=-52;x<=52;x+=2.8){
  const sag=6.2*(1-(x/56)*(x/56));
  const y=deckY+16.5-sag;
  beam(bridge,[x,deckY+.7,z],[x,y,z],.065,steel,7);
 }
}

// Additional tower anchor cables and diagonal stabilizers
for(const side of [-1,1]){
 const z=side*4.5;
 for(const x of [-22,22]){
  for(const end of [x<0?-55:55]){
   beam(bridge,[x,deckY+22,z],[end,deckY+10,z],.14,darkSteel);
  }
 }
}

// Under-deck longitudinal trusses
for(const z of [-5.6,5.6]){
 for(let x=-54;x<54;x+=3){
  beam(bridge,[x,deckY-1,z],[x+3,deckY-1,z],.12,steel);
  beam(bridge,[x,deckY-1,z],[x+3,deckY-2.3,z],.10,darkSteel);
  beam(bridge,[x+3,deckY-1,z],[x,deckY-2.3,z],.10,darkSteel);
 }
}
for(let x=-54;x<=54;x+=4){
 beam(bridge,[x,deckY-1,-5.6],[x,deckY-1,5.6],.11,steel);
}

// Small structural details on tower and deck
for(const x of towerXs){
 for(const z of [-4.5,4.5]){
  for(let y=deckY+3;y<deckY+21;y+=3){
   box(bridge,1.35,.13,1.35,x,y,z,gold);
  }
 }
}

// Subtle environment lighting and ground plane details
const sunDisc=new THREE.Mesh(
 new THREE.SphereGeometry(3,24,16),
 new THREE.MeshBasicMaterial({color:0xffe4bd})
);
sunDisc.position.set(-65,55,-100);scene.add(sunDisc);

// Sensor system
const sensorColors={
 "Temperature":0xff994e,"Vibration":0x48d9ff,"Strain":0xff4d79,
 "Humidity":0x51aaff,"Water Level":0x38d5c1,
 "Displacement":0xc18aff,"Wind Speed":0xffd05c,"Pressure":0x9be56c
};
let sensors=[];
let placing=false,showSensors=true,paused=false,anomaly=false;
let elapsed=0,history=[],lastValues={};

function toast(msg){
 const t=document.getElementById('toast');
 t.textContent=msg;t.style.display='block';
 setTimeout(()=>t.style.display='none',2200);
}
function refreshSensors(){
 document.getElementById('sensorCount').textContent=sensors.length;
 const list=document.getElementById('sensorList');
 if(!sensors.length){list.innerHTML='<div class="small">No sensors placed yet.</div>';return}
 list.innerHTML=sensors.map((s,i)=>
  `<div class="sensor-item"><span style="color:${'#'+sensorColors[s.type].toString(16).padStart(6,'0')}">●</span> ${s.type} · S-${String(i+1).padStart(2,'0')}</div>`
 ).join('');
}
function addSensor(point,type){
 const color=sensorColors[type];
 const group=new THREE.Group();
 const stem=new THREE.Mesh(
  new THREE.CylinderGeometry(.07,.09,.55,10),
  new THREE.MeshStandardMaterial({color:0x263d50,metalness:.8,roughness:.25})
 );
 stem.position.y=.22;group.add(stem);
 const orb=new THREE.Mesh(
  new THREE.SphereGeometry(.25,20,16),
  new THREE.MeshStandardMaterial({color,emissive:color,emissiveIntensity:1.8,metalness:.25,roughness:.2})
 );
 orb.position.y=.58;group.add(orb);
 const ring=new THREE.Mesh(
  new THREE.TorusGeometry(.38,.035,8,32),
  new THREE.MeshBasicMaterial({color})
 );
 ring.rotation.x=Math.PI/2;ring.position.y=.12;group.add(ring);
 group.position.copy(point);group.visible=showSensors;
 bridge.add(group);
 sensors.push({type,group,orb});
 refreshSensors();
 toast(type+' sensor placed');
}

document.getElementById('placeBtn').onclick=()=>{
 placing=true;
 document.getElementById('placeBtn').classList.add('active');
 document.getElementById('hint').style.display='block';
 toast('Click a point on the bridge to place the sensor');
};
document.getElementById('cancelBtn').onclick=()=>{
 placing=false;
 document.getElementById('placeBtn').classList.remove('active');
 document.getElementById('hint').style.display='none';
};
document.getElementById('removeBtn').onclick=()=>{
 if(sensors.length){
  bridge.remove(sensors.pop().group);refreshSensors();toast('Last sensor removed');
 }else toast('There are no sensors to remove');
};
document.getElementById('showBtn').onclick=()=>{
 showSensors=!showSensors;
 sensors.forEach(s=>s.group.visible=showSensors);
 document.getElementById('showBtn').textContent=showSensors?'Hide sensors':'Show sensors';
};
document.getElementById('resetBtn').onclick=()=>{
 sensors.forEach(s=>bridge.remove(s.group));sensors=[];
 anomaly=false;refreshSensors();toast('Sensor layout reset');
};
document.getElementById('pauseBtn').onclick=()=>{
 paused=!paused;
 document.getElementById('pauseBtn').textContent=paused?'▶ Resume':'Ⅱ Pause';
};
document.getElementById('anomalyBtn').onclick=()=>{
 anomaly=true;toast('Simulated abnormality introduced');
};

const raycaster=new THREE.Raycaster();
const pointer=new THREE.Vector2();
const deckTargets=[bridge];
renderer.domElement.addEventListener('pointerdown',e=>{
 if(!placing)return;
 const rect=renderer.domElement.getBoundingClientRect();
 pointer.x=((e.clientX-rect.left)/rect.width)*2-1;
 pointer.y=-((e.clientY-rect.top)/rect.height)*2+1;
 raycaster.setFromCamera(pointer,camera);
 const hits=raycaster.intersectObject(bridge,true);
 if(hits.length){
  const p=hits[0].point.clone();
  addSensor(p,document.getElementById('sensorType').value);
  placing=false;
  document.getElementById('placeBtn').classList.remove('active');
  document.getElementById('hint').style.display='none';
 }
});

// Telemetry
function jitter(base,amount){return base+(Math.random()-.5)*amount}
function updateMetrics(){
 const mult=Number(document.getElementById('speed').value);
 elapsed+=.5*mult;
 const values={
  temperature:jitter(24+Math.sin(elapsed/22)*2,1.1),
  vibration:jitter(.8+Math.sin(elapsed/4)*.25, .25),
  strain:jitter(120+Math.sin(elapsed/10)*10,9),
  humidity:jitter(58+Math.sin(elapsed/18)*5,3),
  water:jitter(2.1+Math.sin(elapsed/30)*.15,.08),
  displacement:jitter(1.2+Math.sin(elapsed/8)*.25,.15),
  wind:jitter(12+Math.sin(elapsed/6)*3,2),
  pressure:jitter(101.3+Math.sin(elapsed/24)*.5,.25)
 };
 if(anomaly){
  values.vibration+=3.5+Math.random()*2;
  values.strain+=75+Math.random()*30;
  values.displacement+=2.2;
 }
 lastValues=values;
 const display={
  temperature:[values.temperature.toFixed(1),'°C'],
  vibration:[values.vibration.toFixed(2),'mm/s'],
  strain:[Math.round(values.strain),'με'],
  humidity:[Math.round(values.humidity),'%'],
  water:[values.water.toFixed(2),'m'],
  displacement:[values.displacement.toFixed(2),'mm'],
  wind:[values.wind.toFixed(1),'km/h'],
  pressure:[values.pressure.toFixed(1),'kPa']
 };
 for(const [key,[val,unit]] of Object.entries(display)){
  document.getElementById(key).innerHTML=val+'<span class="unit">'+unit+'</span>';
 }
 const risk=Math.min(99,Math.round(
  Math.max(0,(values.vibration-1.5)*13)+
  Math.max(0,(values.strain-155)*.22)+
  Math.max(0,(values.displacement-1.8)*8)
 ));
 const alertCount=(risk>=35?1:0)+(risk>=65?1:0);
 document.getElementById('risk').textContent=String(risk).padStart(2,'0')+'%';
 document.getElementById('alerts').textContent=alertCount;
 const box=document.getElementById('healthBox');
 if(risk>=35){
  box.classList.add('alert');
  document.getElementById('healthText').className='bad';
  document.getElementById('healthText').textContent='● SIMULATED ANOMALY';
  document.getElementById('healthDesc').textContent='One or more simulated readings exceed the illustrative thresholds.';
  document.getElementById('aiText').textContent='Rule-based analysis has flagged unusual simulated vibration or strain. Review the readings.';
 }else{
  box.classList.remove('alert');
  document.getElementById('healthText').className='good';
  document.getElementById('healthText').textContent='● NORMAL CONDITION';
  document.getElementById('healthDesc').textContent='Simulated parameters are within illustrative normal ranges.';
  document.getElementById('aiText').textContent='No unusual simulated pattern detected. Continue monitoring the digital twin.';
 }
 history.push(values.vibration);
 if(history.length>90)history.shift();
 drawChart();
}
function drawChart(){
 const canvas=document.getElementById('chart');
 const ctx=canvas.getContext('2d');
 const w=canvas.clientWidth,h=canvas.clientHeight;
 const dpr=Math.min(devicePixelRatio,2);
 canvas.width=w*dpr;canvas.height=h*dpr;
 ctx.scale(dpr,dpr);
 ctx.clearRect(0,0,w,h);
 ctx.strokeStyle='rgba(110,150,180,.18)';ctx.lineWidth=1;
 for(let i=0;i<4;i++){
  const y=10+i*(h-20)/3;
  ctx.beginPath();ctx.moveTo(0,y);ctx.lineTo(w,y);ctx.stroke();
 }
 if(history.length<2)return;
 const max=Math.max(5,...history);
 const min=0;
 const pts=history.map((v,i)=>[
  i/(history.length-1)*w,
  h-10-(v-min)/(max-min)*(h-20)
 ]);
 ctx.beginPath();pts.forEach((p,i)=>i?ctx.lineTo(...p):ctx.moveTo(...p));
 ctx.lineTo(w,h);ctx.lineTo(0,h);ctx.closePath();
 const grad=ctx.createLinearGradient(0,0,0,h);
 grad.addColorStop(0,'rgba(52,197,245,.30)');
 grad.addColorStop(1,'rgba(52,197,245,0)');
 ctx.fillStyle=grad;ctx.fill();
 ctx.beginPath();pts.forEach((p,i)=>i?ctx.lineTo(...p):ctx.moveTo(...p));
 ctx.strokeStyle='#43c8f4';ctx.lineWidth=2;ctx.stroke();
}

// Animation loop
const clock=new THREE.Clock();
function animate(){
 requestAnimationFrame(animate);
 const dt=clock.getDelta();
 if(!paused){
  sensors.forEach(s=>{
   s.orb.scale.setScalar(1+.08*Math.sin(performance.now()*.003));
  });
 }
 controls.update();
 renderer.render(scene,camera);
}
animate();
setInterval(()=>{if(!paused)updateMetrics()},1000);

function resize(){
 camera.aspect=innerWidth/innerHeight;
 camera.updateProjectionMatrix();
 renderer.setSize(innerWidth,innerHeight);
}
window.addEventListener('resize',resize);
refreshSensors();
updateMetrics();
</script>
</body>
</html>
"""

components.html(html, height=1050, scrolling=False)
