/* ==========================================================
   AutoDevAI Premium Charts
========================================================== */

let qualityChart = null;
let distributionChart = null;

/* ==========================================================
Initialize
========================================================== */

window.addEventListener("load", () => {

    createQualityChart();

    createDistributionChart();

});

/* ==========================================================
Repository Quality
========================================================== */

function createQualityChart() {

    const canvas = document.getElementById("scoreChart");

    if (!canvas) return;

    const ctx = canvas.getContext("2d");

    const gradient = ctx.createLinearGradient(0,0,0,400);

    gradient.addColorStop(0,"rgba(59,130,246,.65)");
    gradient.addColorStop(.5,"rgba(124,58,237,.25)");
    gradient.addColorStop(1,"rgba(0,0,0,0)");

    qualityChart = new Chart(ctx,{

        type:"line",

        data:{

            labels:[
                "Planner",
                "Review",
                "Security",
                "Testing",
                "Docs",
                "Final"
            ],

            datasets:[{

                data:[35,58,72,84,92,98],

                fill:true,

                backgroundColor:gradient,

                borderColor:"#4F8CFF",

                borderWidth:4,

                tension:.45,

                pointRadius:6,

                pointHoverRadius:9,

                pointBackgroundColor:"#ffffff",

                pointBorderColor:"#4F8CFF"

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

            animation:{
                duration:1800,
                easing:"easeOutQuart"
            },

            interaction:{
                intersect:false,
                mode:"index"
            },

            scales:{

                x:{
                    grid:{
                        display:false
                    },
                    ticks:{
                        color:"#94A3B8"
                    }
                },

                y:{
                    min:0,
                    max:100,

                    ticks:{
                        color:"#94A3B8"
                    },

                    grid:{
                        color:"rgba(255,255,255,.06)"
                    }

                }

            }

        }

    });

}

/* ==========================================================
Quality Distribution
========================================================== */

function createDistributionChart(){

    const canvas=document.getElementById("doughnutChart");

    if(!canvas) return;

    const ctx=canvas.getContext("2d");

    distributionChart=new Chart(ctx,{

        type:"doughnut",

        data:{

            labels:[

                "Security",
                "Testing",
                "Documentation",
                "Review"

            ],

            datasets:[{

                data:[95,90,96,98],

                backgroundColor:[

                    "#3B82F6",

                    "#22C55E",

                    "#F59E0B",

                    "#8B5CF6"

                ],

                borderWidth:0,

                hoverOffset:18,

                spacing:5

            }]

        },

        options:{

            responsive:true,

            maintainAspectRatio:false,

            cutout:"72%",

            plugins:{

                legend:{

                    position:"bottom",

                    labels:{

                        color:"#CBD5E1",

                        padding:20,

                        usePointStyle:true,

                        pointStyle:"circle"

                    }

                }

            },

            animation:{

                animateRotate:true,

                duration:1800

            }

        },

        plugins:[CenterTextPlugin]

    });

}

/* ==========================================================
Center Text Plugin
========================================================== */

const CenterTextPlugin={

    id:"centerText",

    beforeDraw(chart){

        const {ctx}=chart;

        const width=chart.width;

        const height=chart.height;

        ctx.restore();

        ctx.font="700 40px Inter";

        ctx.fillStyle="#ffffff";

        ctx.textAlign="center";

        ctx.fillText(

            "95",

            width/2,

            height/2-4

        );

        ctx.font="500 14px Inter";

        ctx.fillStyle="#94A3B8";

        ctx.fillText(

            "Overall",

            width/2,

            height/2+24

        );

        ctx.save();

    }

};

/* ==========================================================
Live Update
========================================================== */

function updateCharts(scan){

    if(!scan) return;

    if(qualityChart){

        qualityChart.data.datasets[0].data=[

            scan.score-55,

            scan.score-35,

            scan.security,

            scan.testing,

            scan.documentation,

            scan.score

        ];

        qualityChart.update();

    }

    if(distributionChart){

        distributionChart.data.datasets[0].data=[

            scan.security,

            scan.testing,

            scan.documentation,

            scan.score

        ];

        distributionChart.update();

    }

}

/* ==========================================================
Random Demo Animation
(Removable later)
========================================================== */

setInterval(()=>{

    if(!qualityChart) return;

    qualityChart.data.datasets[0].data=

    qualityChart.data.datasets[0].data.map(v=>{

        let n=v+(Math.random()*4-2);

        n=Math.max(60,Math.min(100,n));

        return Math.round(n);

    });

    qualityChart.update();

},6000);