function getCookie(name) {
    let cookieValue = null;

    if (document.cookie && document.cookie !== "") {
        const cookies = document.cookie.split(";");

        for (let cookie of cookies) {
            cookie = cookie.trim();

            if (cookie.startsWith(name + "=")) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }

    return cookieValue;
}

document.querySelectorAll(".like-btn").forEach(button => {

    button.addEventListener("click", function () {

        const noteId = this.dataset.id;

        fetch(/notes/like/${noteId}, {
            method: "POST",
            headers: {
                "X-CSRFToken": getCookie("csrftoken"),
            }
        })

        .then(response => response.json())

        .then(data => {

            const icon = this.querySelector("i");

            if (data.liked) {
                this.classList.remove("btn-outline-danger");
                this.classList.add("btn-danger");

                icon.classList.remove("bi-heart");
                icon.classList.add("bi-heart-fill");
            } else {
                this.classList.remove("btn-danger");
                this.classList.add("btn-outline-danger");

                icon.classList.remove("bi-heart-fill");
                icon.classList.add("bi-heart");
            }

        })

        .catch(error => {
            console.log(error);
        });

    });

});