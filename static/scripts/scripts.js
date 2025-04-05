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

document.getElementById("year").textContent = new Date().getFullYear();

// Toggle fullscreen functionality
const fullscreenToggles = document.querySelectorAll('.fullscreen-toggle');

fullscreenToggles.forEach(toggle => {
    toggle.addEventListener('click', () => {
        if (!document.fullscreenElement) {
            if (document.documentElement.requestFullscreen) {
                document.documentElement.requestFullscreen();
            } else if (document.documentElement.mozRequestFullScreen) {
                document.documentElement.mozRequestFullScreen();
            } else if (document.documentElement.webkitRequestFullscreen) {
                document.documentElement.webkitRequestFullscreen();
            } else if (document.documentElement.msRequestFullscreen) {
                document.documentElement.msRequestFullscreen();
            }
            
            // Change icon to compress
            fullscreenToggles.forEach(t => {
                const icon = t.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-expand');
                    icon.classList.add('fa-compress');
                }
            });
        } else {
            if (document.exitFullscreen) {
                document.exitFullscreen();
            } else if (document.mozCancelFullScreen) {
                document.mozCancelFullScreen();
            } else if (document.webkitExitFullscreen) {
                document.webkitExitFullscreen();
            } else if (document.msExitFullscreen) {
                document.msExitFullscreen();
            }
            
            // Change icon back to expand
            fullscreenToggles.forEach(t => {
                const icon = t.querySelector('i');
                if (icon) {
                    icon.classList.remove('fa-compress');
                    icon.classList.add('fa-expand');
                }
            });
        }
    });
});

// Mobile sidebar functionality
const mobileMenuToggle = document.getElementById('mobileMenuToggle');
const sidebar = document.getElementById('sidebar');
const closeSidebar = document.getElementById('closeSidebar');
const overlay = document.getElementById('overlay');

mobileMenuToggle.addEventListener('click', () => {
    sidebar.style.right = '0';
    overlay.style.display = 'block';
    document.body.style.overflow = 'hidden'; // Prevent scrolling when sidebar is open
});

function hideSidebar() {
    sidebar.style.right = '-250px';
    overlay.style.display = 'none';
    document.body.style.overflow = ''; // Re-enable scrolling
}

closeSidebar.addEventListener('click', hideSidebar);
overlay.addEventListener('click', hideSidebar);

// Close sidebar when clicking on a menu item (for demo purposes)
const sidebarItems = document.querySelectorAll('.sidebar-item');
sidebarItems.forEach(item => {
    item.addEventListener('click', () => {
        if (window.innerWidth <= 600) {
            hideSidebar();
        }
    });
});