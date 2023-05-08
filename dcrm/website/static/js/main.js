closeBtn = document.querySelector(".close-button")
message = document.querySelector(".the-message")

closeBtn.addEventListener("click", e => {
    message.style.display = "none"
})

