async function checkStatus() {
    const response = await fetch('/status');
    const data = await response.json();
    const statusMessage = document.getElementById('status-message');
    statusMessage.textContent = `Status: ${data.status}`;
}