/* =======================================================
   Academic Notes Organizer - Shared Site Script
   Handles: mobile sidebar toggle, animated bubble background,
   password show/hide, password strength meter, file input preview
   All sections are guarded so this single file works safely
   across every page, whether or not the related element exists.
======================================================= */

document.addEventListener("DOMContentLoaded", function () {

    /* ---------------- Mobile Sidebar Toggle ---------------- */
    const sidebar = document.getElementById("sidebar");
    const sidebarToggle = document.getElementById("sidebarToggle");
    const sidebarOverlay = document.getElementById("sidebarOverlay");

    if (sidebar && sidebarToggle && sidebarOverlay) {

        function openSidebar() {
            sidebar.classList.add("show");
            sidebarOverlay.classList.add("show");
        }

        function closeSidebar() {
            sidebar.classList.remove("show");
            sidebarOverlay.classList.remove("show");
        }

        sidebarToggle.addEventListener("click", function () {
            sidebar.classList.contains("show") ? closeSidebar() : openSidebar();
        });

        sidebarOverlay.addEventListener("click", closeSidebar);

        document.querySelectorAll(".sidebar a").forEach(function (link) {
            link.addEventListener("click", function () {
                if (window.innerWidth <= 992) {
                    closeSidebar();
                }
            });
        });
    }

    /* ---------------- Animated Bubble Background ---------------- */
    const bubbleBg = document.getElementById("bubbleBg");

    if (bubbleBg) {
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
    }

    /* ---------------- Password Show/Hide Toggle (login.html) ---------------- */
    const password = document.getElementById("password");
    const eye = document.querySelector(".bi-eye");

    if (password && eye && eye.parentElement && eye.parentElement.tagName === "BUTTON") {
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
    }

    /* ---------------- Password Strength Meter (register.html) ---------------- */
    if (password) {
        password.addEventListener("keyup", function () {
            const bar = document.querySelector(".progress-bar");
            if (!bar) return;

            const value = password.value.length;

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
    }

    /* ---------------- File Input Preview (create-course.html / create-note.html) ---------------- */
    document.querySelectorAll('input[type="file"]').forEach(function (input) {
        input.addEventListener("change", function () {
            if (this.files.length > 0 && this.previousElementSibling) {
                this.previousElementSibling.innerHTML = this.files[0].name;
            }
        });
    });

    /* ---------------- Sidebar Link Active Highlight on Click (dashboard.html style pages) ---------------- */
    document.querySelectorAll(".sidebar a").forEach(function (link) {
        link.addEventListener("click", function () {
            document.querySelectorAll(".sidebar a").forEach(function (item) {
                item.classList.remove("active");
            });
            this.classList.add("active");
        });
    });

});
