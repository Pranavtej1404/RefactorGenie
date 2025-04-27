async function analyzeCode() {
    const code = document.getElementById("codeInput").value;
    const language = document.getElementById("languageSelect").value;
    
    const response = await fetch("http://127.0.0.1:8000/analyze", {
        method: "POST",
        headers: {
            "Content-Type": "application/json"
        },
        body: JSON.stringify({ code: code, language: language })
    });

    const data = await response.json();

    const output = document.getElementById("suggestionsOutput");
    output.textContent = JSON.stringify(data, null, 2);
}
