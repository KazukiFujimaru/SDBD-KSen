// Handle lesson selection
const lessonItems = document.querySelectorAll('.lesson-item');
const lessonContents = document.querySelectorAll('.lesson-content');
const continueBtn = document.getElementById('continue-btn');

lessonItems.forEach(item => {
    item.addEventListener('click', function() {
        // Remove active class from all lessons
        lessonItems.forEach(li => li.classList.remove('active'));
        
        // Add active class to clicked lesson
        this.classList.add('active');
        
        // Get the lesson ID and link
        const lessonId = this.getAttribute('data-lesson');
        const lessonLink = this.getAttribute('data-link');
        
        // Hide all lesson contents
        lessonContents.forEach(content => {
            content.classList.remove('active');
        });
        
        // Show the selected lesson content
        document.getElementById('content-' + lessonId).classList.add('active');
        
        // Update the continue button link
        continueBtn.href = lessonLink;
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