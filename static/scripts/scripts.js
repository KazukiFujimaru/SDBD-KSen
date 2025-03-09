document.querySelectorAll(".quiz-container").forEach((quizBox) => {
    const submitBtn = quizBox.querySelector(".submit-btn");
    const feedback = quizBox.querySelector(".quiz-feedback");
    const explanation = quizBox.querySelector(".quiz-explanation");
    const hiddenContent = quizBox.nextElementSibling; // Get next hidden content

    submitBtn.addEventListener("click", function() {
        const selectedOption = quizBox.querySelector('input[type="radio"]:checked');

        if (!selectedOption) {
            feedback.innerHTML = "<p style='color: red;'>Please select an answer!</p>";
            return;
        }

        const selectedLabel = selectedOption.parentElement;
        const isCorrect = selectedLabel.getAttribute("data-correct") === "true";

        if (isCorrect) {
            // Correct Answer: Replace quiz with explanation
            quizBox.classList.add("correct");
            quizBox.classList.remove("incorrect", "shake");
            quizBox.innerHTML = explanation.innerHTML;
            
            if (hiddenContent && hiddenContent.classList.contains("hidden-content")) {
                hiddenContent.classList.remove("hidden"); // Reveal the next section
            }
        } else {
            // Incorrect Answer: Apply shake effect & keep red border
            quizBox.classList.add("incorrect", "shake");
            feedback.innerHTML = "<p style='color: red;'>Incorrect! Try again.</p>";

            // Remove shake effect after animation
            setTimeout(() => quizBox.classList.remove("shake"), 500);
        }
    });
});
