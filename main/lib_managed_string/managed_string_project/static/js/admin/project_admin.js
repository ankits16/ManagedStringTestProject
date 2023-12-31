// document.addEventListener('DOMContentLoaded', function() {
//     const sourceChoiceDropdown = document.getElementById('id_source_type');
//     const contentTypeField = document.getElementById('id_content_type');
//     const objectIdField = document.getElementById('id_object_id');

//     if (sourceChoiceDropdown) {
//         console.log('<<<<< sourceChoiceDropdown found')
//         sourceChoiceDropdown.addEventListener('change', function() {
//             const sourceType = sourceChoiceDropdown.value;
//             // Logic to update contentTypeField and objectIdField
//             console.log('<<<< selected choice is ' + sourceType)
//         });
//     } else {
//         console.error('Source choice dropdown not found');
//     }
// });

document.addEventListener("DOMContentLoaded", function() {
    function toggleInlines() {
        var choice = document.getElementById("id_source_type").value;
        // Assuming the inline forms have identifiable IDs or classes
        var githubInline = document.getElementById("githubsource_set-group");
        var fileUploadInline = document.getElementById("fileuploadsource_set-group");
        console.log('<<<<<<<< githubInline = ' + githubInline)
        if (choice == "") {
            fileUploadInline.style.display = "none";
            githubInline.style.display = "none";
        }
        else if (choice == "github") {
            githubInline.style.display = "";
            fileUploadInline.style.display = "none";
        } else if (choice == "file_upload") {
            githubInline.style.display = "none";
            fileUploadInline.style.display = "";
        }
    }

    // Initial toggle on page load
    toggleInlines();

    // Setup event listener
    document.getElementById("id_source_type").addEventListener("change", toggleInlines);
});