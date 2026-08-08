// ===============================
// AutoDevAI Dashboard
// ===============================

let scoreChart = null;

document.addEventListener("DOMContentLoaded", () => {

    loadLatest();

    loadHistory();

});

// ===============================
// Latest Scan
// ===============================

async function loadLatest(){

    try{

        const response = await fetch("/api/latest");

        const data = await response.json();

        updateDashboard(data);

    }

    catch(error){

        console.error(error);

    }

}

// ===============================
// Update Dashboard
// ===============================

function updateDashboard(data){

    document.getElementById("repo").textContent =
        data.repository || "-";

    document.getElementById("language").textContent =
        data.language || "-";

    document.getElementById("files").textContent =
        data.files || 0;

    document.getElementById("security-score").textContent =
        data.security + "%";

    document.getElementById("documentation-score").textContent =
        data.documentation + "%";

    animateHealth(data.score);

    buildScoreChart(data);

}

// ===============================
// Health Ring
// ===============================

function animateHealth(score){

    const value = document.getElementById("healthScore");

    value.innerHTML = score + "%";

    const ring = document.querySelector(".health-ring");

    const angle = score * 3.6;

    ring.style.background =
        `conic-gradient(
            #27D980 ${angle}deg,
            rgba(255,255,255,.08) ${angle}deg
        )`;

}

// ===============================
// Chart
// ===============================

function buildScoreChart(data){

    const ctx =
        document
        .getElementById("scoreChart")
        .getContext("2d");

    if(scoreChart){

        scoreChart.destroy();

    }

    scoreChart = new Chart(ctx,{

        type:"radar",

        data:{

            labels:[

                "Overall",
                "Security",
                "Testing",
                "Documentation"

            ],

            datasets:[{

                label:"Repository",

                data:[

                    data.score,

                    data.security,

                    data.testing,

                    data.documentation

                ],

                borderColor:"#4F7CFF",

                backgroundColor:"rgba(79,124,255,.20)",

                pointRadius:4,

                borderWidth:3

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

                    suggestedMin:0,

                    suggestedMax:100,

                    grid:{

                        color:"rgba(255,255,255,.08)"

                    },

                    angleLines:{

                        color:"rgba(255,255,255,.08)"

                    },

                    pointLabels:{

                        color:"#cbd5e1"

                    },

                    ticks:{

                        backdropColor:"transparent",

                        color:"#94a3b8"

                    }

                }

            }

        }

    });

}

// ===============================
// History
// ===============================

async function loadHistory(){

    try{

        const response =
            await fetch("/api/history");

        const rows =
            await response.json();

        const body =
            document.querySelector(
                "#historyTable tbody"
            );

        body.innerHTML = "";

        rows.forEach(scan=>{

            body.innerHTML += `

            <tr>

                <td>${scan.repository}</td>

                <td>${scan.score}%</td>

                <td>${scan.security}%</td>

                <td>${scan.created_at}</td>

            </tr>

            `;

        });

    }

    catch(error){

        console.log(error);

    }

}

// ===============================
// Counter Animation
// ===============================

function animateNumber(id,target){

    const element =
        document.getElementById(id);

    let current = 0;

    const timer = setInterval(()=>{

        current++;

        element.textContent=current;

        if(current>=target){

            clearInterval(timer);

        }

    },15);

}