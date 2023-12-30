document.addEventListener('DOMContentLoaded', function() {
    const sourceChoiceDropdown = document.getElementById('id_source_choice');
    const contentTypeField = document.getElementById('id_content_type');
    const objectIdField = document.getElementById('id_object_id');

    sourceChoiceDropdown.addEventListener('change', function() {
        // Logic to update contentTypeField and objectIdField
        // based on the selected source type
        console.log('<<<<<<< change is called')
    });
});