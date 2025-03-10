document.querySelectorAll(".quiz-container").forEach((quizBox) => {
    const submitBtn = quizBox.querySelector(".submit-btn");
    const feedback = quizBox.querySelector(".quiz-feedback");
    const explanation = quizBox.querySelector(".quiz-explanation");
    const hiddenContent = quizBox.nextElementSibling; // Get the next hidden content

    submitBtn.addEventListener("click", function() {
        const selectedOption = quizBox.querySelector('input[type="radio"]:checked');

        if (!selectedOption) {
            feedback.innerHTML = "<p style='color: red;'>Tolong pilih salah satu jawaban</p>";
            return;
        }

        const selectedLabel = selectedOption.parentElement;
        const isCorrect = selectedLabel.getAttribute("data-correct") === "true";

        if (isCorrect) {
            // Correct Answer: Replace quiz with explanation
            quizBox.classList.add("correct");
            quizBox.classList.remove("incorrect", "shake");
            quizBox.innerHTML = explanation.innerHTML;

            // Reveal hidden content (if any)
            if (hiddenContent && hiddenContent.classList.contains("hidden-content")) {
                hiddenContent.classList.remove("hidden");
            }

            // Find and reveal the next hidden quiz
            const nextQuiz = quizBox.parentElement.querySelector(".quiz-container.hidden");
            if (nextQuiz) {
                nextQuiz.classList.remove("hidden");
            }
        } else {
            // Incorrect Answer: Apply shake effect & keep red border
            quizBox.classList.add("incorrect", "shake");
            feedback.innerHTML = "<p style='color: red;'>Jawaban kurang tepat. Coba lagi.</p>";

            // Remove shake effect after animation
            setTimeout(() => quizBox.classList.remove("shake"), 500);
        }
    });
});

document.querySelectorAll(".accordion-header").forEach(button => {
    button.addEventListener("click", function() {
        const accordion = this.parentElement;
        accordion.classList.toggle("open");
    });
});
