
function resetForm() {
    const form = document.getElementById('queryForm');
  
    form.reset();
  }
  
  function clearForm() {
    const form = document.getElementById('queryForm');
  
    form.elements['input_text'].value = '';
    form.elements['regex_pattern'].value = '';
  }
  