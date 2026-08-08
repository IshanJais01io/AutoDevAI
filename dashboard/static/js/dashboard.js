
function resetDashboard(){

    updateMetric("repo","-");

    updateMetric("language","-");

    updateMetric("files","0");

    updateMetric("security-score","0%");

    updateMetric("documentation-score","0%");

    const health=document.getElementById("healthScore");

    if(health){

        health.textContent="0%";

    }

    const ring = document.querySelector(".health-ring");

if(ring){

    ring.style.background =
        "conic-gradient(var(--green) 0deg, var(--green) 0deg, rgba(255,255,255,.08) 0deg, rgba(255,255,255,.08) 360deg)";

}

    const status = document.getElementById("scanStatus");

if(status){

    status.textContent = "Ready";

    status.style.color = "#94a3b8";

}

const progress = document.getElementById("progressBar");

if(progress){

    progress.style.width = "0%";

}

    renderFindings([]);

    renderRecommendations([]);

    document.querySelectorAll(".scan-steps div").forEach(step=>{

    step.classList.remove("active");

    step.classList.remove("completed");

});

}

/* ==========================================================
   AutoDevAI Dashboard
========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    attachHoverEffects();

    resetDashboard();

    const scanButton=document.getElementById("scanButton");

    if(scanButton){

        scanButton.addEventListener("click",startRepositoryScan);

    }

    const search=document.getElementById("repoSearch");

    if(search){

        search.addEventListener("input",filterRepository);

    }
const download=document.getElementById("downloadReport");

if(download){

    download.onclick=()=>{

        window.location="/api/download-report";

    };

}
    initializeEditor();

}); let editor=null;
window.showAllFindings=false;

/* ==========================================================
   Counter Animation
========================================================== */

function animateValue(element, endValue, suffix = "") {

    if (!element) return;

    let start = 0;

    const duration = 1400;

    const stepTime = 16;

    const increment = endValue / (duration / stepTime);

    function update() {

        start += increment;

        if (start >= endValue) {

            element.textContent = endValue + suffix;

            return;

        }

        element.textContent = Math.floor(start) + suffix;

        requestAnimationFrame(update);

    }

    update();

}

function animateNumbers() {

    const cards = document.querySelectorAll(".metric-card h3");

    cards.forEach(card => {

        const text = card.textContent.trim();

        const value = parseInt(text.replace(/\D/g, ""));

        if (!isNaN(value)) {

            const suffix = text.includes("%") ? "%" : "";

            animateValue(card, value, suffix);

        }

    });

}

/* ==========================================================
   Health Ring
========================================================== */

function animateHealthRing() {

    const score = document.getElementById("healthScore");

    const ring = document.querySelector(".health-ring");

    if (!score || !ring) return;

    const value = parseInt(score.textContent) || 0;

    animateValue(score, value, "%");

    const angle = (value / 100) * 360;

    ring.style.background =
        `conic-gradient(
            var(--green) 0deg,
            var(--green) ${angle}deg,
            rgba(255,255,255,.08) ${angle}deg,
            rgba(255,255,255,.08) 360deg
        )`;

}

/* ==========================================================
   Fake Scan Progress Animation
========================================================== */

function animateProgress() {

    const progress = document.getElementById("progressBar");

    if (!progress) return;

    const steps = [

        "step1",
        "step2",
        "step3",
        "step4",
        "step5",
        "step6"

    ];

    let width = 0;

    let index = 0;

    const timer = setInterval(() => {

        width += 17;

        progress.style.width = width + "%";

        if (steps[index]) {

            const el = document.getElementById(steps[index]);

            if (el) {

                el.style.background = "#2563eb";

                el.style.color = "white";

                el.style.fontWeight = "700";

            }

        }

        index++;

        if (width >= 100) {

            clearInterval(timer);

            const status = document.getElementById("scanStatus");

            if (status) {

                status.textContent = "Ready";

                status.style.color = "#22c55e";

            }

        }

    }, 500);

}

/* ==========================================================
   Card Hover
========================================================== */

function attachHoverEffects() {

    document.querySelectorAll(".metric-card").forEach(card => {

        card.addEventListener("mouseenter", () => {

            card.style.transform = "translateY(-8px) scale(1.02)";

        });

        card.addEventListener("mouseleave", () => {

            card.style.transform = "";

        });

    });

}

/* ==========================================================
   Refresh Dashboard
========================================================== */

async function refreshDashboard() {

    try {

        const response = await fetch("/api/latest");

        const data = await response.json();

        updateMetric("repo", data.repository);

        updateMetric("language", data.language);

        updateMetric("files", data.files);

        updateMetric("security-score", data.security + "%");

        updateMetric("documentation-score", data.documentation + "%");

    }

    catch (err) {

        console.log(err);

    }

}

function updateMetric(id, value) {

    const el = document.getElementById(id);

    if (el) {

        el.textContent = value;

    }

}

/* ==========================================================
   Smooth Scroll
========================================================== */

document.querySelectorAll("a[href^='#']").forEach(link => {

    link.addEventListener("click", e => {

        e.preventDefault();

        const target = document.querySelector(link.getAttribute("href"));

        if (target) {

            target.scrollIntoView({

                behavior: "smooth"

            });

        }

    });

});

/* ==========================================================
   Floating Background Glow
========================================================== */

setInterval(() => {

    document.querySelectorAll(".glass-card").forEach(card => {

        card.style.boxShadow =

            "0 0 " +

            (20 + Math.random() * 20) +

            "px rgba(79,140,255,.18)";

    });

}, 2500);

/* ==========================================================
   Live Dashboard Loader
========================================================== */

async function loadDashboard() {

    try {

        const response = await fetch("/api/dashboard");

        const data = await response.json();

        updateDashboard(data);

    }

    catch (e) {

        console.error(e);

    }

}


function updateDashboard(data){

    updateMetric("repo", data.repository);
    updateMetric("language", data.language);
    updateMetric("files", data.files);

    updateMetric("security-score", data.security + "%");
    updateMetric("documentation-score", data.documentation + "%");

    const health=document.getElementById("healthScore");
    if(health){
        health.textContent=data.health + "%";
    }

    animateHealthRing();

    const overall=document.getElementById("overallScore");
    if(overall){
        overall.textContent=data.score + "%";
    }

    const securityLabel=document.getElementById("securityLabel");
    if(securityLabel){
        securityLabel.textContent=data.security + "%";
    }

    const testingLabel=document.getElementById("testingLabel");
    if(testingLabel){
        testingLabel.textContent=data.testing + "%";
    }

    const documentationLabel=document.getElementById("documentationLabel");
    if(documentationLabel){
        documentationLabel.textContent=data.documentation + "%";
    }

    const performanceLabel=document.getElementById("performanceLabel");
    if(performanceLabel){
performanceLabel.textContent=data.performance + "%";    }

    const quality=document.getElementById("qualityScore");

if(quality){

    quality.textContent=data.score+"%";

}

    document.querySelector(".fill.green").style.width =
        data.security + "%";

    document.querySelector(".fill.blue").style.width =
        data.testing + "%";

    document.querySelector(".fill.purple").style.width =
        data.documentation + "%";

    document.querySelector(".fill.orange").style.width =
        data.score + "%";

    renderRecommendations(data.recommendations);

    renderFindings(data.findings);

    loadChart(data);

}


function renderRecommendations(items){

    const grid=document.getElementById("recommendationGrid");

    if(!grid) return;

    grid.innerHTML="";
    if(items.length===0){

    grid.innerHTML=`

    <div class="empty-state">

        Run a repository scan to generate AI recommendations.

    </div>

    `;

    return;

}

    items.forEach(item=>{

        grid.innerHTML+=`

        <div class="recommend-card">

            <div class="recommend-top">

                <span class="recommend-badge ${item.priority.toLowerCase()}">

                    ${item.priority}

                </span>

                <span>${item.category}</span>

            </div>

            <h3>${item.title}</h3>

            <p>${item.description}</p>

            <div class="recommend-bottom">

                <span>${item.impact}</span>

                <span>${item.eta}</span>

            </div>

        </div>

        `;

    });

}


async function loadRepository() {

    const container=document.getElementById("repositoryTree");

    if(!container) return;

    if(!window.repositoryLoaded){

        container.innerHTML="";

        return;

    }

async function loadFolder(path, parent) {

    const response = await fetch(
        "/api/repository?path=" + encodeURIComponent(path)
    );

    const items = await response.json();

    items.forEach(item => {

        const row = document.createElement("div");

        row.className = "repo-row";

        row.innerHTML = `
            <span class="repo-toggle">
                ${item.folder ? "▶" : ""}
            </span>

            <span class="repo-icon">

            ${getFileIcon(item)}

            </span>

            <span class="repo-name">
                ${item.name}
            </span>
        `;

        parent.appendChild(row);

        if (item.folder) {

            const children = document.createElement("div");

            children.className = "repo-children";

            parent.appendChild(children);

            let opened = false;

            row.onclick = async () => {

                if (!opened) {

                    children.innerHTML = "";

                    await loadFolder(item.path, children);

                    children.style.display="block";
                    

children.animate(

[
    {

        opacity:0,

        transform:"translateY(-6px)"

    },

    {

        opacity:1,

        transform:"translateY(0)"

    }

],

{

    duration:180

}

);

                    row.querySelector(".repo-toggle").textContent = "▼";

                    row.querySelector(".repo-icon").innerHTML = '<i class="fa-solid fa-folder-open"></i>';

                    opened = true;

                }

                else {

                    children.style.display =
                        children.style.display === "none"
                        ? "block"
                        : "none";

                    row.querySelector(".repo-toggle").textContent =
                        children.style.display === "none"
                        ? "▶"
                        : "▼";

                    row.querySelector(".repo-icon").innerHTML =
    children.style.display === "none"
    ? '<i class="fa-solid fa-folder"></i>'
    : '<i class="fa-solid fa-folder-open"></i>';

                }

            };

        }

        else {

            row.onclick = () => previewFile(item.path);

        }

    });

}

container.innerHTML = "";

await loadFolder("", container);

}

function getFileIcon(item){

    if(item.folder){

        return '<i class="fa-solid fa-folder"></i>';

    }

    const file=item.name.toLowerCase();

    if(file.endsWith(".py"))
        return '<i class="fa-brands fa-python file-python"></i>';

    if(file.endsWith(".js"))
        return '<i class="fa-brands fa-js file-js"></i>';

    if(file.endsWith(".html"))
        return '<i class="fa-brands fa-html5 file-html"></i>';

    if(file.endsWith(".css"))
        return '<i class="fa-brands fa-css3-alt file-css"></i>';

    if(file.endsWith(".json"))
        return '<i class="fa-solid fa-code file-json"></i>';

    if(file.endsWith(".md"))
        return '<i class="fa-solid fa-book file-md"></i>';

    if(file.endsWith(".yml") || file.endsWith(".yaml"))
        return '<i class="fa-solid fa-gears file-yaml"></i>';

    return '<i class="fa-solid fa-file file-default"></i>';

}

/* ==========================================================
   File Preview
========================================================== */

async function previewFile(path){

    try{

        document.getElementById("fileBreadcrumb").textContent = path.split(/[\\/]/).join("  ›  ").replaceAll("/"," > ");

        const response = await fetch(
            "/api/file?path=" + encodeURIComponent(path)
        );

        const text = await response.text();

        const viewer = document.getElementById("fileViewer");

        viewer.className = "";

        if(path.endsWith(".py"))
            viewer.classList.add("language-python");

        else if(path.endsWith(".js"))
            viewer.classList.add("language-javascript");

        else if(path.endsWith(".html"))
            viewer.classList.add("language-xml");

        else if(path.endsWith(".css"))
            viewer.classList.add("language-css");

        else if(path.endsWith(".json"))
            viewer.classList.add("language-json");

        else
            viewer.classList.add("language-plaintext");

        if(editor){

    editor.setValue(text);

}

else{

    viewer.textContent=text;

}

        const totalLines = text.split("\n").length;

let numbers = "";

for(let i=1;i<=totalLines;i++){

    numbers += i + "\n";

}

document.getElementById("lineNumbers").textContent = numbers;

        const downloadButton =

document.getElementById("downloadButton");

if(downloadButton){

    downloadButton.onclick=()=>{

        const blob=new Blob([text]);

        const url=URL.createObjectURL(blob);

        const a=document.createElement("a");

        a.href=url;

        a.download=path.split("/").pop();

        a.click();

        URL.revokeObjectURL(url);

    };

}

        hljs.highlightElement(viewer);

viewer.parentElement.scrollTop = 0;

document.getElementById("lineNumbers").scrollTop = 0;

    }

    catch(err){

        console.error(err);

    }

}


/* ==========================================================
   Copy Button
========================================================== */

document.addEventListener("DOMContentLoaded",()=>{

    const copy=document.getElementById("copyButton");

if(copy){

    copy.onclick=()=>{

        navigator.clipboard.writeText(

            editor
            ?editor.getValue()
            :document
            .getElementById("fileViewer")
            .textContent

        );

        copy.textContent="Copied ✓";

        setTimeout(()=>{

            copy.textContent="📋 Copy";

        },1500);

    };

}

    const repoSearch =
    document.getElementById("repoSearch");

    if(copy){

        copy.onclick = ()=>{

            navigator.clipboard.writeText(

                document.getElementById("fileViewer").textContent

            );

        };

    }
    if(repoSearch){

    repoSearch.addEventListener(

        "keyup",

        ()=>{

            filterRepository(

                repoSearch.value

            );

        }

    );

}

});

document.addEventListener("DOMContentLoaded",()=>{

    const search=document.getElementById("repoSearch");

    if(!search) return;

    search.addEventListener("keyup",()=>{

        const value=search.value.toLowerCase();

        document.querySelectorAll(".repo-row").forEach(row=>{

            row.style.display=

                row.innerText.toLowerCase().includes(value)

                ?

                "flex"

                :

                "none";

        });

    });

});

/* ==========================================================
   Repository Search
========================================================== */

function filterRepository(){

    const search=document
        .getElementById("repoSearch")
        .value
        .toLowerCase();

    document
    .querySelectorAll(".repo-row")
    .forEach(row=>{

        const name=row
        .querySelector(".repo-name")
        .textContent
        .toLowerCase();

        row.style.display=
            name.includes(search)
            ?"flex"
            :"none";

    });

}

/* ==========================================================
   Sidebar Active Menu
========================================================== */

document
.querySelector(".sidebar nav")
.addEventListener("click",e=>{

    const link=e.target.closest(".nav-link");

    if(!link) return;

    document
    .querySelectorAll(".nav-link")
    .forEach(l=>l.classList.remove("active"));

    link.classList.add("active");

});

const codeArea=document.querySelector(".code-container pre");

const lineArea=document.getElementById("lineNumbers");

if(codeArea){

    codeArea.addEventListener("scroll",()=>{

        lineArea.scrollTop=codeArea.scrollTop;

    });

}

function renderFindings(items){

    const tbody=document.getElementById("findingsTable");

    if(!tbody) return;

    if(!items || items.length===0){

        tbody.innerHTML=`
        <tr>
            <td colspan="5" style="text-align:center;padding:40px;">
                No findings available.
            </td>
        </tr>
        `;

        return;
    }

    let visible=items.slice(0,5);

    tbody.innerHTML="";

    visible.forEach(item=>{

        let color="green";

        if(item.severity==="High") color="red";
        else if(item.severity==="Medium") color="yellow";

        tbody.innerHTML+=`
        <tr>

            <td>
                <span class="badge ${color}">
                    ${item.severity}
                </span>
            </td>

            <td>${item.file}</td>

            <td>${item.category}</td>

            <td>${item.confidence}%</td>

            <td>${item.recommendation}</td>

        </tr>
        `;

    });

    let old=document.getElementById("viewAllFindings");

    if(old) old.remove();

    if(items.length>5){

        const button=document.createElement("button");

        button.id="viewAllFindings";

        button.className="view-findings-btn";

        button.innerHTML="🔍 View All Findings ("+items.length+")";

        button.onclick=function(){

            tbody.innerHTML="";

            items.forEach(item=>{

                let color="green";

                if(item.severity==="High") color="red";
                else if(item.severity==="Medium") color="yellow";

                tbody.innerHTML+=`
                <tr>

                    <td>
                        <span class="badge ${color}">
                            ${item.severity}
                        </span>
                    </td>

                    <td>${item.file}</td>

                    <td>${item.category}</td>

                    <td>${item.confidence}%</td>

                    <td>${item.recommendation}</td>

                </tr>
                `;

            });

            button.remove();

        };

        document.querySelector(".findings-card")
        .appendChild(button);

    }

}

function loadChart(data){

    const canvas=document.getElementById("scoreChart");

    if(!canvas) return;

    if(window.scoreChart){

try{

window.scoreChart.destroy();

}

catch(e){

console.log(e);

}

window.scoreChart=null;

}

    window.scoreChart=new Chart(canvas,{

        type:"radar",

        data:{

            labels:[
                "Security",
                "Testing",
                "Documentation",
                "Performance",
                "Quality"
            ],

            datasets:[{

                label:"Repository Score",

                data:[
                    data.security,
                    data.testing,
                    data.documentation,
                    data.score,
                    data.health
                ],

                fill:true

            }]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            plugins:{

                legend:{
                    display:false
                }

            },

            scales:{

                r:{
                    min:0,
                    max:100
                }

            }

        }

    });

}

let qualityChart=null;

function renderScoreChart(data){

    const ctx=document
        .getElementById("scoreChart");

    if(!ctx) return;

    if(qualityChart){

        qualityChart.destroy();

    }

    qualityChart=new Chart(ctx,{

        type:"radar",

        data:{

            labels:[

                "Security",

                "Testing",

                "Documentation",

                "Performance",

                "Overall"

            ],

            datasets:[{

                label:"Repository Score",

                data:[

                    data.security,

                    data.testing,

                    data.documentation,

                    data.performance,

                    data.score

                ],

                fill:true,

                borderWidth:3

            }]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            scales:{

                r:{

                    suggestedMin:0,

                    suggestedMax:100

                }

            }

        }

    });

}

async function openFinding(file, line){

    await previewFile(file);

    setTimeout(() => {

        highlightLine(line);

    }, 300);

}

function highlightLine(line){

    const viewer = document.getElementById("fileViewer");

    if(!viewer) return;

    const text = viewer.textContent;

    const lines = text.split("\n");

    if(line <= lines.length){

        lines[line-1] =
            "👉 " + lines[line-1];

    }

    viewer.textContent = lines.join("\n");

}

function initializeEditor(){

    require.config({

        paths:{

            vs:"https://cdn.jsdelivr.net/npm/monaco-editor@0.52.2/min/vs"

        }

    });

    require(

        ["vs/editor/editor.main"],

        function(){

            editor=monaco.editor.create(

                document.getElementById("fileViewer"),

                {

                    value:"",

                    language:"python",

                    readOnly:true,

                    theme:"vs-dark",

                    automaticLayout:true,

                    minimap:{

                        enabled:false

                    }

                }

            );

        }

    );

}

document
.querySelector(".sidebar nav")
.addEventListener("click",e=>{

    const link=e.target.closest(".nav-link");

    if(!link) return;

    document
    .querySelectorAll(".nav-link")
    .forEach(l=>l.classList.remove("active"));

    link.classList.add("active");

});

async function startRepositoryScan(){

    const input=document.getElementById("repoInput");

    if(!input) return;

    const repo=input.value.trim();

    if(repo===""){

        alert("Please enter a GitHub repository.");

        return;

    }

    const button=document.getElementById("scanButton");

    button.disabled=true;

    button.textContent="Scanning...";

    try{

        const response=await fetch("/api/scan",{

            method:"POST",

            headers:{

                "Content-Type":"application/json"

            },

            body:JSON.stringify({

                repository:repo

            })

        });

        if(!response.ok){

            throw new Error("Scan failed");

        }

        resetDashboard();

await loadDashboard();
animateProgress();
window.repositoryLoaded = true;

await loadDashboard();

await loadRepository();

alert("Analysis completed successfully.");

    }

    catch(err){

        console.error(err);

        alert("Repository scan failed.");

    }

    finally{

        button.disabled=false;

        button.textContent="Analyze Repository";

    }

}

document
.getElementById("downloadReport")
.onclick=()=>{

window.open("/reports/final_report.html");

};
