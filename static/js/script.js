let autocorrectEnabled = true;
let autocorrectTimeout;
const editorDiv = document.getElementById('editor');
document.getElementById('toggleAutocorrect').addEventListener('click', function() {
  autocorrectEnabled = !autocorrectEnabled;
  this.textContent = `Autocorrect: ${autocorrectEnabled ? 'ON' : 'OFF'}`;
});
editorDiv.addEventListener('keyup', function(event) {
  if (!autocorrectEnabled) return;
  if (event.key === " ") {
    clearTimeout(autocorrectTimeout);
    autocorrectTimeout = setTimeout(() => {
      let text = editorDiv.innerText;
      fetch('/autocorrect', {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({ text: text })
      })
      .then(response => response.json())
      .then(data => {
        editorDiv.innerText = data.correctedText;
        placeCaretAtEnd(editorDiv);
      })
      .catch(error => console.error('Autocorrect error:', error));
    }, 500);
  }
});
function placeCaretAtEnd(el) {
  el.focus();
  if (typeof window.getSelection !== "undefined" && typeof document.createRange !== "undefined") {
    let range = document.createRange();
    range.selectNodeContents(el);
    range.collapse(false);
    let sel = window.getSelection();
    sel.removeAllRanges();
    sel.addRange(range);
  }
}
function formatText(command) {
  document.execCommand(command, false, null);
}
document.getElementById('saveBtn').addEventListener('click', function() {
  let content = editorDiv.innerText;
  let fileName = prompt("Enter file name:", "document");
  if (!fileName) {
    return;
  }
  let blob = new Blob([content], { type: 'text/plain' });
  let url = URL.createObjectURL(blob);
  let a = document.createElement('a');
  a.href = url;
  a.download = fileName + ".txt";
  document.body.appendChild(a);
  a.click();
  document.body.removeChild(a);
});
