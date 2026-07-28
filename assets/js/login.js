const password = document.getElementById("password");

const eye = document.querySelector(".bi-eye");

eye.parentElement.addEventListener("click", function () {

    if (password.type === "password") {

        password.type = "text";

        eye.classList.remove("bi-eye");

        eye.classList.add("bi-eye-slash");

    } else {

        password.type = "password";

        eye.classList.remove("bi-eye-slash");

        eye.classList.add("bi-eye");

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
