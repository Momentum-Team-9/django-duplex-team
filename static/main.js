let showAnswer = document.querySelectorAll(".answerButton")

for (button of showAnswer){
let id = button.getAttribute("id")

button.addEventListener("click", function() {
    let answer = document.querySelector("#a" + id)
    if (answer.classList.contains("show")) {
        answer.classList.remove("show")
    } else {
        answer.classList.add("show")
    }
})
}