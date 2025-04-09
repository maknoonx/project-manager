// projects/static/projects/js/confirm_delete.js

document.addEventListener('DOMContentLoaded', function() {
    // Find all delete project buttons
    const deleteButtons = document.querySelectorAll('.delete-project');
    
    // Add click event listener to each button
    deleteButtons.forEach(button => {
        button.addEventListener('click', function(e) {
            // Get project name from data attribute
            const projectName = this.getAttribute('data-project-name');
            
            // Show confirmation dialog
            if (!confirm(`هل أنت متأكد من حذف المشروع "${projectName}"؟`)) {
                // If user cancels, prevent the link from being followed
                e.preventDefault();
            }
        });
    });
});