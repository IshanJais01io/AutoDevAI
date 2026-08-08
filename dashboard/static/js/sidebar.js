/* ==========================================================
   AutoDevAI Premium Sidebar
========================================================== */

document.addEventListener("DOMContentLoaded", () => {

    initializeSidebar();

    initializeKeyboardShortcut();

    initializeMobileSidebar();

});

/* ==========================================================
Sidebar Initialization
========================================================== */

function initializeSidebar(){

    const items=document.querySelectorAll(".sidebar nav a");

    const current=localStorage.getItem("activePage");

    if(current){

        items.forEach(item=>{

            if(item.dataset.page===current){

                item.classList.add("active");

            }

        });

    }

    items.forEach(item=>{

        item.addEventListener("click",function(e){

            e.preventDefault();

            activateItem(this);

        });

    });

}

/* ==========================================================
Active State
========================================================== */

function activateItem(item){

    document

    .querySelectorAll(".sidebar nav a")

    .forEach(link=>{

        link.classList.remove("active");

    });

    item.classList.add("active");

    localStorage.setItem(

        "activePage",

        item.dataset.page

    );

    smoothTransition();

    navigate(item.dataset.page);

}

/* ==========================================================
Fake Navigation
Replace later with real pages
========================================================== */

function navigate(page){

    switch(page){

        case "dashboard":

            console.log("Dashboard");

            break;

        case "review":

            console.log("AI Review");

            break;

        case "security":

            console.log("Security");

            break;

        case "testing":

            console.log("Testing");

            break;

        case "documentation":

            console.log("Documentation");

            break;

        case "reports":

            console.log("Reports");

            break;

        case "history":

            console.log("History");

            break;

        case "settings":

            console.log("Settings");

            break;

    }

}

/* ==========================================================
Fade Transition
========================================================== */

function smoothTransition(){

    const content=document.querySelector(".content");

    if(!content) return;

    content.style.opacity="0";

    content.style.transform="translateY(15px)";

    setTimeout(()=>{

        content.style.transition=".35s";

        content.style.opacity="1";

        content.style.transform="translateY(0px)";

    },120);

}

/* ==========================================================
Collapse Sidebar
========================================================== */

function toggleSidebar(){

    document

    .querySelector(".app-layout")

    .classList

    .toggle("collapsed");

}

/* ==========================================================
Keyboard Shortcut
Ctrl + B
========================================================== */

function initializeKeyboardShortcut(){

    document.addEventListener("keydown",e=>{

        if(e.ctrlKey && e.key.toLowerCase()==="b"){

            e.preventDefault();

            toggleSidebar();

        }

    });

}

/* ==========================================================
Mobile
========================================================== */

function initializeMobileSidebar(){

    const menu=document.getElementById("mobileMenu");

    if(!menu) return;

    menu.addEventListener("click",()=>{

        toggleSidebar();

    });

}

/* ==========================================================
Hover Animation
========================================================== */

document

.querySelectorAll(".sidebar nav a")

.forEach(item=>{

    item.addEventListener("mouseenter",()=>{

        item.style.transform="translateX(8px)";

    });

    item.addEventListener("mouseleave",()=>{

        item.style.transform="";

    });

});

/* ==========================================================
Ripple Effect
========================================================== */

document

.querySelectorAll(".sidebar nav a")

.forEach(item=>{

    item.addEventListener("click",function(e){

        const ripple=document.createElement("span");

        ripple.className="ripple";

        ripple.style.left=e.offsetX+"px";

        ripple.style.top=e.offsetY+"px";

        this.appendChild(ripple);

        setTimeout(()=>{

            ripple.remove();

        },600);

    });

});