
import streamlit as st
import streamlit.components.v1 as components

st.set_page_config(
    page_title="BridgeGuard AI | Digital Twin",
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
iframe {border:0!important;}
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
 "imports":{
  "three":"https://cdn.jsdelivr.net/npm/three@0.160.0/build/three.module.js",
  "three/addons/":"https://cdn.jsdelivr.net/npm/three@0.160.0/examples/jsm/"
 }
}
</script>

<style>
*{box-sizing:border-box}
html,body{
 margin:0;width:100%;height:100%;overflow:hidden;
 font-family:Arial,sans-serif;color:#eafaff;
 background:#83b9d5
}
#world{position:fixed;inset:0}
#world canvas{width:100%;height:100%;display:block}

.glass{
 position:absolute;z-index:4;
 background:linear-gradient(145deg,
 rgba(5,24,43,.88),rgba(10,49,72,.72));
 border:1px solid rgba(126,218,255,.38);
 border-radius:13px;
 box-shadow:0 12px 35px rgba(0,20,40,.3),
 inset 0 1px rgba(255,255,255,.12);
 backdrop-filter:blur(16px);
 padding:13px;
 color:#effaff;
}
#header{
 top:12px;left:14px;right:14px;height:66px;
 display:flex;align-items:center;justify-content:space-between;
 padding:10px 18px;
}
.logo{font-size:17px;font-weight:900;letter-spacing:1.2px}
.kicker{font-size:9px;color:#9dddf4;letter-spacing:2px;margin-top:5px}
.headright{display:flex;gap:8px;align-items:center}
.tag{
 padding:8px 10px;border-radius:20px;
 background:#1b536e88;border:1px solid #8ddfff44;
 font-size:9px;white-space:nowrap
}
.green{color:#65f0b3}
#left{
 left:14px;top:92px;width:245px;
 max-height:calc(100vh - 225px);overflow:auto
}
#right{
 right:14px;top:92px;width:270px;
 max-height:calc(100vh - 225px);overflow:auto
}
.heading{
 font-size:10px;letter-spacing:1.5px;
 color:#9bdff8;font-weight:900;margin-bottom:12px
}
.section{
 font-size:9px;letter-spacing:1.2px;color:#86cce8;
 margin:13px 0 8px;padding-top:10px;
 border-top:1px solid #ffffff25
}
label{
 display:flex;justify-content:space-between;
 font-size:10px;color:#c6e4f1;margin:9px 0 5px
}
output{color:white;font-weight:bold}
input[type=range]{width:100%;accent-color:#40d9ee}
select{
 width:100%;padding:8px;background:#12354a;color:white;
 border:1px solid #52849d;border-radius:7px;font-size:10px
}
button{
 background:linear-gradient(120deg,#087c9d,#20b9cb);
 border:1px solid #6ce3f0;color:white;
 border-radius:7px;padding:9px 7px;
 font-size:9px;font-weight:900;cursor:pointer
}
button:hover{filter:brightness(1.2)}
button.secondary{background:#173e56}
.buttons{display:flex;gap:7px;margin-top:9px}
.buttons button{flex:1}
.metricgrid{display:grid;grid-template-columns:1fr 1fr;gap:7px}
.metric{
 padding:9px;border:1px solid #a6ddf022;
 border-radius:8px;background:#356f892e
}
.metricname{font-size:8px;color:#a9d1e3;letter-spacing:.6px}
.metricvalue{font-size:20px;font-weight:900;margin-top:5px}
.unit{font-size:8px;color:#9bc4d8}
.sensor{
 display:flex;justify-content:space-between;
 padding:7px 0;border-bottom:1px solid #ffffff18;
 font-size:9px;color:#c5deeb
}
.on{color:#5de9ae;font-weight:900}
.off{color:#f2bd82;font-weight:900}
.alert{
 padding:9px;border-radius:8px;font-size:9px;line-height:1.6;
 background:#185c594f;border:1px solid #52d7ae55;margin-top:8px
}
.warning{background:#9b63344c;border-color:#ffbd7655}
#bottom{
 bottom:12px;left:14px;right:14px;min-height:100px;
 display:grid;grid-template-columns:1fr 1fr 1.6fr 1fr;gap:12px
}
.bottomlabel{
 font-size:8px;color:#9dd6ed;letter-spacing:1.5px;margin-bottom:8px
}
.big{font-size:20px;font-weight:900}
.muted{font-size:9px;color:#a9cbdc;margin-top:5px}
#chart{width:100%;height:53px}
#chart polyline{fill:none;stroke:#59e0ef;stroke-width:2}
#chart polygon{fill:#49cde522}
#hint{
 position:absolute;z-index:3;bottom:120px;right:295px;
 font-size:9px;color:#153c50;background:#e8f7f8bb;
 padding:7px 10px;border-radius:7px
}
#disclaimer{
 position:absolute;z-index:3;bottom:120px;left:50%;
 transform:translateX(-50%);font-size:8px;color:#163c50;
 background:#eaf8f5bb;padding:6px 10px;border-radius:20px;
 white-space:nowrap
}
#loading{
 position:absolute;inset:0;z-index:10;display:grid;
 place-content:center;text-align:center;color:#153a50;
 background:linear-gradient(#94cce9,#d5e9df);
 font-size:17px;font-weight:900
}
#loading small{font-size:10px;font-weight:500;margin-top:10px}
#toast{
 display:none;position:absolute;z-index:12;top:88px;left:50%;
 transform:translateX(-50%);background:#123b51;
 padding:9px 15px;border-radius:8px;font-size:10px
}
#sensorMode{
 font-size:9px;color:#9ee9ff;margin-top:8px;line-height:1.5
}
@media(max-width:850px){
 #left{width:215px;left:8px}
 #right{width:225px;right:8px}
 #bottom{left:8px;right:8px;grid-template-columns:1fr 1fr}
 #header{left:8px;right:8px}
}
@media(max-width:600px){
 #left{top:85px;width:47%;max-height:43vh;left:6px}
 #right{top:85px;width:47%;max-height:43vh;right:6px}
 #bottom{max-height:25vh;overflow:auto}
 .logo{font-size:10px}
 .tag{font-size:7px;padding:6px}
 #disclaimer,#hint{display:none}
}
</style>
</head>

<body>
<div id="world"></div>

<div id="loading">
 BRIDGEGUARD AI
 <small>Constructing 3D structural digital twin...</small>
</div>
<div id="toast"></div>

<div id="header" class="glass">
 <div>
  <div class="logo">BRIDGEGUARD AI</div>
  <div class="kicker">INTELLIGENT STRUCTURAL MONITORING · DIGITAL TWIN</div>
 </div>
 <div class="headright">
  <div class="tag"><span class="green">●</span> SYSTEM ONLINE</div>
  <div class="tag" id="mode">LIVE SIMULATION</div>
  <div class="tag" id="clock">00:00:00</div>
 </div>
</div>

<div id="left" class="glass">
 <div class="heading">01 / SIMULATION CONTROL</div>

 <label>Vehicle weight <output id="weightV">18 t</output></label>
 <input id="weight" type="range" min="5" max="45" value="18">

 <label>Vehicle speed <output id="speedV">55 km/h</output></label>
 <input id="speed" type="range" min="10" max="110" value="55">

 <label>Traffic volume <output id="trafficV">65%</output></label>
 <input id="traffic" type="range" min="0" max="100" value="65">

 <div class="section">STRUCTURAL CHANGE SCENARIO</div>

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

 <div class="section">SENSOR CONFIGURATION</div>
 <label>Sensor type</label>
 <select id="sensorType">
  <option>Temperature</option>
  <option>Vibration</option>
  <option>Strain</option>
  <option>Humidity</option>
  <option>Water Level</option>
  <option>Displacement</option>
  <option>Wind Speed</option>
  <option>Pressure</option>
 </select>

 <div id="sensorMode">
  Select a sensor, then click directly on the bridge to place it.
 </div>

 <div class="buttons">
  <button id="placeMode">PLACE SENSOR</button>
  <button id="clearSensors" class="secondary">CLEAR</button>
 </div>

 <div class="section">SYSTEM CONTROLS</div>
 <div class="buttons">
  <button id="run">Ⅱ PAUSE</button>
  <button id="reset" class="secondary">↺ RESET</button>
 </div>
 <div class="buttons">
  <button id="addVehicle">＋ VEHICLE</button>
  <button id="camera" class="secondary">CAMERA RESET</button>
 </div>
 <div class="buttons">
  <button id="abnormality">GENERATE ALERT</button>
 </div>
</div>

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

 <div class="section">03 / SENSOR NETWORK</div>
 <div class="sensor"><span>Primary sensors</span><b class="on">ONLINE</b></div>
 <div class="sensor"><span>Placed sensors</span><b id="placedCount" class="on">0</b></div>
 <div class="sensor"><span>Strain gauges</span><b class="on">ACTIVE</b></div>
 <div class="sensor"><span>Accelerometers</span><b class="on">ACTIVE</b></div>
 <div class="sensor"><span>Temperature sensors</span><b class="on">ACTIVE</b></div>

 <div class="section">04 / AI EVENT ANALYSIS</div>
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
  Normal simulated operating pattern. Monitoring active.
 </div>

 <div class="section">05 / ADDITIONAL READINGS</div>
 <div class="sensor"><span>Tilt estimate</span><b id="tilt">0.02°</b></div>
 <div class="sensor"><span>Humidity</span><b id="humidity">68%</b></div>
 <div class="sensor"><span>Corrosion proxy</span><b id="corrosion">Low</b></div>
 <div class="sensor"><span>Crack-width proxy</span><b id="crack">0.00 mm</b></div>
 <div class="sensor"><span>Acoustic activity</span><b id="acoustic">Low</b></div>
 <div class="sensor"><span>Joint displacement</span><b id="joint">0.30 mm</b></div>
</div>

<div id="hint">DRAG TO ORBIT · SCROLL TO ZOOM · CLICK TO PLACE SENSORS</div>
<div id="disclaimer">
 EDUCATIONAL SIMULATION · NOT A REAL BRIDGE SAFETY SYSTEM
</div>

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
  <div class="muted" id="responseNote">Within simulated baseline</div>
 </div>
 <div>
  <div class="bottomlabel">SENSOR HISTORY / RESPONSE TREND</div>
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
   <button id="sensorToggle" class="secondary">HIDE SENSORS</button>
  </div>
  <div class="muted" id="exportStatus">Live data collection</div>
 </div>
</div>

<script type="module">
import * as THREE from 'three';
import {OrbitControls} from 'three/addons/controls/OrbitControls.js';
import {Sky} from 'three/addons/objects/Sky.js';

const root=document.getElementById('world');
const scene=new THREE.Scene();
scene.background=new THREE.Color(0x8bbfda);
scene.fog=new THREE.Fog(0x9bcde2,450,1300);

const camera=new THREE.PerspectiveCamera(
 43,innerWidth/innerHeight,.1,5000
);
camera.position.set(210,145,270);

const renderer=new THREE.WebGLRenderer({antialias:true});
renderer.setPixelRatio(Math.min(devicePixelRatio,2));
renderer.setSize(innerWidth,innerHeight);
renderer.shadowMap.enabled=true;
renderer.shadowMap.type=THREE.PCFSoftShadowMap;
renderer.outputColorSpace=THREE.SRGBColorSpace;
renderer.toneMapping=THREE.ACESFilmicToneMapping;
renderer.toneMappingExposure=1.25;
root.appendChild(renderer.domElement);

const controls=new OrbitControls(camera,renderer.domElement);
controls.enableDamping=true;
controls.dampingFactor=.055;
controls.maxPolarAngle=Math.PI*.49;
controls.minDistance=45;
controls.maxDistance=850;
controls.target.set(0,38,0);

scene.add(new THREE.HemisphereLight(0xdaf5ff,0x64745c,2.2));

const sun=new THREE.DirectionalLight(0xfff0d7,3.5);
sun.position.set(-200,300,170);
sun.castShadow=true;
sun.shadow.mapSize.set(2048,2048);
sun.shadow.camera.left=-400;
sun.shadow.camera.right=400;
sun.shadow.camera.top=400;
sun.shadow.camera.bottom=-400;
scene.add(sun);

const sky=new Sky();
sky.scale.setScalar(4500);
sky.material.uniforms.turbidity.value=5;
sky.material.uniforms.rayleigh.value=2.5;
sky.material.uniforms.mieCoefficient.value=.004;
sky.material.uniforms.mieDirectionalG.value=.8;
sky.material.uniforms.sunPosition.value.copy(sun.position).normalize();
scene.add(sky);

function material(color,roughness=.55,metalness=.25){
 return new THREE.MeshStandardMaterial({
  color,roughness,metalness
 });
}

const steel=material(0x879eaa,.3,.8);
const concrete=material(0xb8c4c9,.8,.1);
const cableMat=material(0xc8d9df,.3,.75);
const roadMat=material(0x303a43,.9,.05);
const laneMat=material(0xe9e6d8,.7,.05);
const waterMat=new THREE.MeshStandardMaterial({
 color:0x176d91,roughness:.24,metalness:.38,
 envMapIntensity:1
});

const water=new THREE.Mesh(
 new THREE.PlaneGeometry(4000,4000),waterMat
);
water.rotation.x=-Math.PI/2;
water.position.y=-12;
water.receiveShadow=true;
scene.add(water);

const bridge=new THREE.Group();
scene.add(bridge);

const sensorGroup=new THREE.Group();
scene.add(sensorGroup);

const vehicleGroup=new THREE.Group();
scene.add(vehicleGroup);

const L=300,W=27,Y=35;
const raycaster=new THREE.Raycaster();
const pointer=new THREE.Vector2();

let placedSensors=[];
let vehicleObjects=[];
let active=true;
let showSensors=true;
let placeMode=false;
let elapsed=0;
let history=[];
let records=[];
let abnormality=false;

function box(parent,x,y,z,sx,sy,sz,mat){
 const mesh=new THREE.Mesh(
  new THREE.BoxGeometry(sx,sy,sz),mat
 );
 mesh.position.set(x,y,z);
 mesh.castShadow=true;
 mesh.receiveShadow=true;
 parent.add(mesh);
 return mesh;
}

function cable(parent,a,b,r,mat){
 const direction=new THREE.Vector3().subVectors(b,a);
 const mesh=new THREE.Mesh(
  new THREE.CylinderGeometry(r,r,direction.length(),10),
  mat
 );
 mesh.position.copy(a).add(b).multiplyScalar(.5);
 mesh.quaternion.setFromUnitVectors(
  new THREE.Vector3(0,1,0),direction.normalize()
 );
 mesh.castShadow=true;
 parent.add(mesh);
}

function tube(parent,points,r,mat){
 const curve=new THREE.CatmullRomCurve3(points);
 const mesh=new THREE.Mesh(
  new THREE.TubeGeometry(curve,160,r,8,false),mat
 );
 mesh.castShadow=true;
 parent.add(mesh);
 return mesh;
}

// Main bridge deck
box(bridge,0,Y,0,L,2.4,W,roadMat);
box(bridge,0,Y-1.5,0,L,1,W+2,steel);

// Road markings
for(let x=-L/2+5;x<L/2;x+=12){
 box(bridge,x,Y+1.23,0,5,.045,.18,laneMat);
}

// Side railings and deck supports
for(const z of [-W/2-1,W/2+1]){
 box(bridge,0,Y+2,z,L,.45,.65,steel);
 box(bridge,0,Y+4,z,L,.2,.25,concrete);

 for(let x=-L/2;x<=L/2;x+=6){
  box(bridge,x,Y+3,z,.22,1.35,.22,steel);
 }
}

// Main suspension towers
for(const x of [-65,65]){
 for(const z of [-8,8]){
  box(bridge,x,Y+46,z,4.2,94,4.2,concrete);
  box(bridge,x,Y+46,z,5,2,5,steel);
 }
 box(bridge,x,Y+92,0,5,4,20,steel);
 box(bridge,x,Y+47,0,4,2,18,steel);
}

// Suspension cables, two sides
for(const z of [-10,10]){
 const points=[];
 for(let i=0;i<=100;i++){
  const x=-150+i*3;
  const sag=Y+97-58*Math.pow(x/150,2);
  points.push(new THREE.Vector3(x,sag,z));
 }
 tube(bridge,points,.42,cableMat);

 // Vertical hangers
 for(let x=-145;x<=145;x+=6){
  const sag=Y+97-58*Math.pow(x/150,2);
  cable(
   bridge,
   new THREE.Vector3(x,Y+3,z),
   new THREE.Vector3(x,sag,z),
   .12,steel
  );
 }
}

// Main cross cables
for(const x of [-65,65]){
 cable(
  bridge,
  new THREE.Vector3(x,Y+94,-10),
  new THREE.Vector3(x,Y+94,10),
  .45,cableMat
 );
}

// Under-deck cross beams
for(let x=-145;x<=145;x+=12){
 box(bridge,x,Y-2,0,1.2,3,W,steel);
}

// Piers
for(const x of [-65,65]){
 for(const z of [-8,8]){
  box(bridge,x,-3,z,7,70,7,concrete);
 }
}

// Distant landscape
const landMat=material(0x607e68,1,0);
for(let i=0;i<24;i++){
 const hill=new THREE.Mesh(
  new THREE.SphereGeometry(1,28,18),landMat
 );
 hill.scale.set(60+(i%5)*25,12+(i%4)*7,65);
 hill.position.set(-600+i*52,-4,i%2===0?-260:290);
 scene.add(hill);
}

// Clouds
const cloudMat=new THREE.MeshStandardMaterial({
 color:0xffffff,roughness:1,transparent:true,opacity:.83
});
for(let i=0;i<35;i++){
 const cloud=new THREE.Group();
 const count=4+Math.floor(Math.random()*5);
 for(let j=0;j<count;j++){
  const puff=new THREE.Mesh(
   new THREE.SphereGeometry(1,16,12),cloudMat
  );
  puff.scale.set(
   9+Math.random()*14,
   5+Math.random()*7,
   8+Math.random()*12
  );
  puff.position.set(
   j*12-count*5,
   Math.random()*5,
   Math.random()*10
  );
  cloud.add(puff);
 }
 cloud.position.set(
  (Math.random()-.5)*1100,
  120+Math.random()*130,
  -250-Math.random()*500
 );
 scene.add(cloud);
}

// Sensor visuals
function sensorColor(type){
 const colors={
  Temperature:0xffa34a,
  Vibration:0x00e5ff,
  Strain:0x42f58d,
  Humidity:0xd76cff,
  "Water Level":0xffd447,
  Displacement:0xff5d68,
  "Wind Speed":0x70aaff,
  Pressure:0xffffff
 };
 return colors[type]||0x00e5ff;
}

function addSensor(point,type){
 const color=sensorColor(type);
 const group=new THREE.Group();

 const core=new THREE.Mesh(
  new THREE.SphereGeometry(1.05,20,20),
  new THREE.MeshStandardMaterial({
   color,emissive:color,emissiveIntensity:1.7,
   metalness:.2,roughness:.25
  })
 );
 group.add(core);

 const ring=new THREE.Mesh(
  new THREE.TorusGeometry(1.8,.09,8,28),
  new THREE.MeshBasicMaterial({
   color,transparent:true,opacity:.85
  })
 );
 ring.rotation.x=Math.PI/2;
 group.add(ring);

 group.position.copy(point);
 group.userData.type=type;
 sensorGroup.add(group);
 placedSensors.push({type,position:point.clone(),object:group});
 document.getElementById('placedCount').textContent=placedSensors.length;
}

function buildDefaultSensors(){
 for(let i=0;i<24;i++){
  const x=-135+i*11.7;
  addSensor(new THREE.Vector3(x,Y+3,0),'Strain');
 }
 sensorGroup.visible=showSensors;
}
buildDefaultSensors();

// Vehicles
function createVehicle(){
 const group=new THREE.Group();

 const body=new THREE.Mesh(
  new THREE.BoxGeometry(10,3.4,4.5),
  material(0xe5e9ed,.3,.5)
 );
 body.position.y=3;
 body.castShadow=true;
 group.add(body);

 const cabin=new THREE.Mesh(
  new THREE.BoxGeometry(4,2.6,4.2),
  material(0x8db7c8,.2,.5)
 );
 cabin.position.set(-2,5.8,0);
 group.add(cabin);

 const wheelMat=material(0x17212a,.9,0);
 for(const x of [-3.5,3.5]){
  for(const z of [-2.15,2.15]){
   const wheel=new THREE.Mesh(
    new THREE.CylinderGeometry(1,1,.55,20),wheelMat
   );
   wheel.rotation.x=Math.PI/2;
   wheel.position.set(x,1.2,z);
   group.add(wheel);
  }
 }

 vehicleGroup.add(group);
 vehicleObjects.push({mesh:group,p:Math.random()});
 document.getElementById('count').textContent=
  'Vehicles: '+vehicleObjects.length;
}
createVehicle();

// User interaction: click bridge surface to place sensor
renderer.domElement.addEventListener('pointerdown',event=>{
 if(!placeMode)return;

 const rect=renderer.domElement.getBoundingClientRect();
 pointer.x=((event.clientX-rect.left)/rect.width)*2-1;
 pointer.y=-((event.clientY-rect.top)/rect.height)*2+1;

 raycaster.setFromCamera(pointer,camera);
 const hits=raycaster.intersectObjects(bridge.children,true);

 if(hits.length){
  const hit=hits[0];
  addSensor(
   hit.point.clone().add(new THREE.Vector3(0,1.5,0)),
   document.getElementById('sensorType').value
  );
  toast('Sensor placed: '+document.getElementById('sensorType').value);
  placeMode=false;
  document.getElementById('placeMode').textContent='PLACE SENSOR';
  document.getElementById('sensorMode').textContent=
   'Sensor placed. Select another type to place another.';
 }
});

function toast(message){
 const e=document.getElementById('toast');
 e.textContent=message;
 e.style.display='block';
 setTimeout(()=>e.style.display='none',2200);
}

function val(id){
 return Number(document.getElementById(id).value);
}
function put(id,value){
 document.getElementById(id).textContent=value;
}

function labels(){
 put('weightV',val('weight')+' t');
 put('speedV',val('speed')+' km/h');
 put('trafficV',val('traffic')+'%');
 put('stiffV',val('stiff')+'%');
 put('localV',val('local')+'%');
 put('trafficBig',val('traffic')+'%');
}
['weight','speed','traffic','stiff','local'].forEach(id=>{
 document.getElementById(id).addEventListener('input',labels);
});
labels();

function drawHistory(value){
 history.push(value);
 if(history.length>60)history.shift();

 const points=history.map((n,i)=>{
  const x=i/(Math.max(1,history.length-1))*400;
  const y=49-Math.min(n/40,1)*43;
  return x+','+y;
 }).join(' ');

 document.getElementById('line').setAttribute('points',points);
 document.getElementById('fill').setAttribute(
  'points','0,52 '+points+' 400,52'
 );
}

// Educational simulated AI analysis
function analyze(){
 const weight=val('weight')/45;
 const speed=val('speed')/110;
 const traffic=val('traffic')/100;
 const structuralChange=
  val('stiff')/30*.75+val('local')/100*.55;

 const load=weight*speed*traffic;
 const deviation=structuralChange*100+load*3;
 const deflection=.7+load*4.4+structuralChange*5.2;
 const strain=72+load*110+structuralChange*180;
 const vibration=.03+load*.34+structuralChange*.2;
 const temperature=27+Math.sin(elapsed/25)*1.5;

 put('deflection',deflection.toFixed(2));
 put('strain',strain.toFixed(0));
 put('vibration',vibration.toFixed(2));
 put('temperature',temperature.toFixed(1));
 put('deviation',deviation.toFixed(1)+'%');
 put('persistence',
  structuralChange>.3?'ELEVATED':
  structuralChange>.08?'MODERATE':'LOW'
 );

 put('tilt',(0.02+structuralChange*.6).toFixed(2)+'°');
 put('humidity',(68+Math.sin(elapsed/30)*2).toFixed(1)+'%');
 put('corrosion',structuralChange>.6?'Elevated proxy':'Low');
 put('crack',(structuralChange*.28).toFixed(2)+' mm');
 put('acoustic',structuralChange>.3?'Elevated':'Low');
 put('joint',(0.3+structuralChange*1.4).toFixed(2)+' mm');

 const alert=document.getElementById('alert');

 if(abnormality||structuralChange>.3){
  alert.className='alert warning';
  alert.textContent=
   'AI ALERT: Unusual simulated structural response detected. '+
   'Additional inspection attention recommended.';
  put('response','ALERT');
  put('responseNote','Simulated abnormality detected');
 }else if(load>.4){
  alert.className='alert';
  alert.textContent=
   'Elevated temporary traffic-load response. Comparing with baseline.';
  put('response','LOAD');
  put('responseNote','Temporary simulated load response');
 }else{
  alert.className='alert';
  alert.textContent=
   'Normal simulated operating pattern. Primary monitoring active.';
  put('response','NORMAL');
  put('responseNote','Within simulated baseline');
 }

 drawHistory(deflection);

 records.push({
  time:elapsed,
  vehicleWeight:val('weight'),
  vehicleSpeed:val('speed'),
  traffic:val('traffic'),
  deflection,
  strain,
  vibration,
  temperature,
  deviation,
  structuralChange
 });

 if(records.length>2000)records.shift();
}

document.getElementById('placeMode').onclick=()=>{
 placeMode=!placeMode;
 put('placeMode',placeMode?'CLICK BRIDGE NOW':'PLACE SENSOR');
 put('sensorMode',placeMode?
  'Placement mode active. Click on the visible bridge deck or tower.':
  'Placement mode off.'
 );
 renderer.domElement.style.cursor=placeMode?'crosshair':'grab';
};

document.getElementById('clearSensors').onclick=()=>{
 sensorGroup.clear();
 placedSensors=[];
 document.getElementById('placedCount').textContent='0';
 buildDefaultSensors();
 toast('Default sensor network restored');
};

document.getElementById('run').onclick=()=>{
 active=!active;
 put('run',active?'Ⅱ PAUSE':'▶ RUN');
 toast(active?'Simulation resumed':'Simulation paused');
};

document.getElementById('reset').onclick=()=>{
 elapsed=0;
 history=[];
 records=[];
 abnormality=false;
 ['stiff','local'].forEach(id=>{
  document.getElementById(id).value=0;
 });
 labels();
 analyze();
 toast('Simulation reset');
};

document.getElementById('addVehicle').onclick=()=>{
 createVehicle();
 toast('Vehicle added');
};

document.getElementById('camera').onclick=()=>{
 camera.position.set(210,145,270);
 controls.target.set(0,38,0);
 controls.update();
};

document.getElementById('abnormality').onclick=()=>{
 abnormality=true;
 analyze();
 toast('Simulated abnormality generated');
};

document.getElementById('sensorToggle').onclick=()=>{
 showSensors=!showSensors;
 sensorGroup.visible=showSensors;
 put('sensorToggle',showSensors?'HIDE SENSORS':'SHOW SENSORS');
};

document.getElementById('export').onclick=()=>{
 if(!records.length){
  toast('Run the simulation first');
  return;
 }

 const keys=Object.keys(records[0]);
 const csv=[
  keys.join(','),
  ...records.map(row=>keys.map(k=>row[k]).join(','))
 ].join('\\n');

 const link=document.createElement('a');
 link.href=URL.createObjectURL(
  new Blob([csv],{type:'text/csv'})
 );
 link.download='BridgeGuard-AI-monitoring-data.csv';
 link.click();
 put('exportStatus','CSV exported');
};

const clock=new THREE.Clock();

function animate(){
 requestAnimationFrame(animate);

 const dt=Math.min(clock.getDelta(),.05);

 if(active){
  elapsed+=dt;

  vehicleObjects.forEach(vehicle=>{
   vehicle.p+=dt*(val('speed')/110)*.08;
   if(vehicle.p>1.1)vehicle.p=-.1;

   const x=(vehicle.p-.5)*L*.85;
   vehicle.mesh.position.set(x,Y+1,0);
  });

  if(Math.floor(elapsed*2)!==Math.floor((elapsed-dt)*2)){
   analyze();
  }
 }

 put('clock',new Date(Math.floor(elapsed)*1000)
  .toISOString().slice(11,19));

 controls.update();
 renderer.render(scene,camera);
}

analyze();
document.getElementById('loading').style.display='none';
animate();

addEventListener('resize',()=>{
 camera.aspect=innerWidth/innerHeight;
 camera.updateProjectionMatrix();
 renderer.setSize(innerWidth,innerHeight);
});
</script>
</body>
</html>
"""

components.html(html, height=1050, scrolling=False)
