
document.querySelectorAll('input[type="file"]').forEach(function(input){

input.addEventListener("change",function(){

if(this.files.length){

this.previousElementSibling.innerHTML=this.files[0].name;

}

});

});

// Mobile Sidebar Toggle

const sidebar=document.getElementById("sidebar");

const sidebarToggle=document.getElementById("sidebarToggle");

const sidebarOverlay=document.getElementById("sidebarOverlay");

function openSidebar(){

sidebar.classList.add("show");

sidebarOverlay.classList.add("show");

}

function closeSidebar(){

sidebar.classList.remove("show");

sidebarOverlay.classList.remove("show");

}

sidebarToggle.addEventListener("click",()=>{

sidebar.classList.contains("show")?closeSidebar():openSidebar();

});

sidebarOverlay.addEventListener("click",closeSidebar);

document.querySelectorAll(".sidebar a").forEach(link=>{

link.addEventListener("click",function(){

if(window.innerWidth<=992){

closeSidebar();

}

});

});

// Generate floating bubbles background

const bubbleBg=document.getElementById("bubbleBg");

const bubbleCount=16;

for(let i=0;i<bubbleCount;i++){

const b=document.createElement("span");

const size=Math.random()*90+20;

b.style.width=size+"px";

b.style.height=size+"px";

b.style.left=Math.random()*100+"%";

b.style.setProperty("--drift",(Math.random()*160-80)+"px");

b.style.animationDuration=(Math.random()*14+14)+"s";

b.style.animationDelay=(Math.random()*-20)+"s";

bubbleBg.appendChild(b);

}