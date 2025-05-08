const uploadForm = document.getElementById('uploadForm');
const pasteForm = document.getElementById('pasteForm');
const resultsDiv = document.getElementById('results');
const dropArea = document.getElementById('drop-area');

// Handle file upload
uploadForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const fileInput = document.getElementById('fileInput');
    if (!fileInput.files.length) return alert("Please select a file.");
    const formData = new FormData();
    formData.append('file', fileInput.files[0]);

    const res = await fetch('/analyze', {
        method: 'POST',
        body: formData
    });
    const data = await res.json();
    displaySuggestions(data.suggestions);
});

// Handle pasted code
pasteForm.addEventListener('submit', async (e) => {
    e.preventDefault();
    const code = document.getElementById('codeInput').value;
    const res = await fetch('/analyze_pasted', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ code })
    });
    const data = await res.json();
    displaySuggestions(data.suggestions);
});

// Handle drag and drop
dropArea.addEventListener('dragover', (e) => {
    e.preventDefault();
    dropArea.classList.add('dragover');
});

dropArea.addEventListener('dragleave', () => {
    dropArea.classList.remove('dragover');
});

dropArea.addEventListener('drop', async (e) => {
    e.preventDefault();
    dropArea.classList.remove('dragover');
    const file = e.dataTransfer.files[0];
    if (!file.name.endsWith('.py')) {
        alert('Please drop a .py file only.');
        return;
    }
    const formData = new FormData();
    formData.append('file', file);
    const res = await fetch('/analyze', {
        method: 'POST',
        body: formData
    });
    const data = await res.json();
    displaySuggestions(data.suggestions);
});

function displaySuggestions(suggestions) {
    if (!suggestions.length) {
        resultsDiv.innerHTML = "<p>No issues found!</p>";
        return;
    }
    resultsDiv.innerHTML = "<h2>Suggestions:</h2><ul>" +
        suggestions.map(s => `<li>${s}</li>`).join('') + "</ul>";
}
