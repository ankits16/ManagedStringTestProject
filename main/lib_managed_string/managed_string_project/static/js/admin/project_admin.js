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
    function toggleSourceForm() {
        
        const sourceType = document.getElementById("id_source_type").value;
        const githubForm = document.getElementById("githubsource_set-group");
        const fileUploadForm = document.getElementById("fileuploadsource_set-group");
        console.log('<<<<< toggleSourceForm called ' + sourceType)
        if (sourceType === "") {
            console.log('<<<<< hide both')
            fileUploadForm.style.display = "none";
            githubForm.style.display = "none";
        }
        else if (sourceType === "github") {
            githubForm.style.display = "block";
            fileUploadForm.style.display = "none";
        } else if (sourceType === "file_upload") {
            githubForm.style.display = "none";
            fileUploadForm.style.display = "block";
        }
    }

    const sourceTypeDropdown = document.getElementById("id_source_type");
    sourceTypeDropdown.addEventListener("change", toggleSourceForm);
    toggleSourceForm(); // Call on initial load
});
