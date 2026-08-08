const scanButton = document.getElementById("scanButton");
const repoInput = document.getElementById("repoInput");

const progressBar = document.getElementById("progressBar");
const scanStatus = document.getElementById("scanStatus");

const steps = [
    "step1",
    "step2",
    "step3",
    "step4",
    "step5",
    "step6"
];

function activateStep(index) {

    const el = document.getElementById(steps[index]);

    if (el) {

        el.classList.add("active");

    }

    progressBar.style.width = ((index + 1) / steps.length) * 100 + "%";

}

function resetProgress() {

    progressBar.style.width = "0%";

    steps.forEach(id => {

        const el = document.getElementById(id);

        if (el) {

            el.classList.remove("active");

        }

    });

}

async function refreshDashboard() {

    const response = await fetch("/api/latest");

    const data = await response.json();

    document.getElementById("repo").innerText =
        data.repository;

    document.getElementById("language").innerText =
        data.language;

    document.getElementById("files").innerText =
        data.files;

    document.getElementById("security-score").innerText =
        data.security + "%";

    document.getElementById("documentation-score").innerText =
        data.documentation + "%";

}

scanButton.addEventListener("click", async () => {

    const repo = repoInput.value.trim();

    if (!repo) {

        alert("Enter GitHub Repository URL");

        return;

    }

    scanButton.disabled = true;

    scanStatus.innerText = "Starting...";

    resetProgress();

    try {

        const response = await fetch("/api/scan", {

            method: "POST",

            headers: {

                "Content-Type": "application/json"

            },

            body: JSON.stringify({

                repository: repo

            })

        });

        if (!response.ok) {

            throw new Error();

        }

        for (let i = 0; i < steps.length; i++) {

            activateStep(i);

            scanStatus.innerText =
                document.getElementById(steps[i]).innerText;

            await new Promise(resolve =>
                setTimeout(resolve, 800)
            );

        }

        scanStatus.innerText = "Completed";

        await refreshDashboard();

    }

    catch {

        alert("Scan failed.");

        scanStatus.innerText = "Failed";

    }

    scanButton.disabled = false;

});