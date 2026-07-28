const password = document.getElementById("password");

password.addEventListener("keyup", function () {

    let value = password.value.length;

    let bar = document.querySelector(".progress-bar");

    if (value < 5) {

        bar.style.width = "30%";
        bar.className = "progress-bar bg-danger";
        bar.innerHTML = "Weak";

    } else if (value < 8) {

        bar.style.width = "60%";
        bar.className = "progress-bar bg-warning";
        bar.innerHTML = "Medium";

    } else {

        bar.style.width = "100%";
        bar.className = "progress-bar bg-success";
        bar.innerHTML = "Strong";

    }

});

// Generate floating bubbles background

const bubbleBg = document.getElementById("bubbleBg");

const bubbleCount = 16;

for (let i = 0; i < bubbleCount; i++) {

    const b = document.createElement("span");

    const size = Math.random() * 90 + 20;

    b.style.width = size + "px";

    b.style.height = size + "px";

    b.style.left = Math.random() * 100 + "%";

    b.style.setProperty("--drift", (Math.random() * 160 - 80) + "px");

    b.style.animationDuration = (Math.random() * 14 + 14) + "s";

    b.style.animationDelay = (Math.random() * -20) + "s";

    bubbleBg.appendChild(b);

}
