document.addEventListener('DOMContentLoaded', function() {
    const sourceChoiceDropdown = document.getElementById('id_source_type');
    const contentTypeField = document.getElementById('id_content_type');
    const objectIdField = document.getElementById('id_object_id');

    if (sourceChoiceDropdown) {
        console.log('<<<<< sourceChoiceDropdown found')
        sourceChoiceDropdown.addEventListener('change', function() {
            const sourceType = sourceChoiceDropdown.value;
            // Logic to update contentTypeField and objectIdField
            console.log('<<<< selected choice is ' + sourceType)
        });
    } else {
        console.error('Source choice dropdown not found');
    }
});