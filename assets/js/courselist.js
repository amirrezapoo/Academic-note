// Fade animation for cards
document.querySelectorAll('.course-card').forEach((card, index) => {
    card.style.opacity = "0";
    card.style.transform = "translateY(25px)";
    setTimeout(() => {
        card.style.transition = ".6s";
        card.style.opacity = "1";
        card.style.transform = "translateY(0)";
    }, index * 100);
});

// Sidebar active state + close on mobile after nav
document.querySelectorAll(".sidebar a").forEach(link => {
    link.addEventListener("click", function () {
        document.querySelectorAll(".sidebar a").forEach(item => item.classList.remove("active"));
        this.classList.add("active");
        if (window.innerWidth <= 992) {
            closeSidebar();
        }
    });
});

// Mobile sidebar toggle
const sidebar = document.getElementById("sidebar");
const sidebarToggle = document.getElementById("sidebarToggle");
const sidebarOverlay = document.getElementById("sidebarOverlay");

function openSidebar() {
    sidebar.classList.add("show");
    sidebarOverlay.classList.add("show");
}

function closeSidebar() {
    sidebar.classList.remove("show");
    sidebarOverlay.classList.remove("show");
}

sidebarToggle.addEventListener("click", () => {
    sidebar.classList.contains("show") ? closeSidebar() : openSidebar();
});

sidebarOverlay.addEventListener("click", closeSidebar);

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