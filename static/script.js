function downloadPdf() {
    const divToDownload = document.getElementById('content');
    const clonedDiv = divToDownload.cloneNode(true);
    const newWindow = window.open('', '_blank');
    newWindow.document.body.appendChild(clonedDiv);
    newWindow.print();
}

function copyPageLink() {
    const tempTextarea = document.createElement('textarea');
    tempTextarea.value = window.location.href;
    document.body.appendChild(tempTextarea);
    tempTextarea.select();
    tempTextarea.setSelectionRange(0, 99999);
    document.execCommand('copy');
    document.body.removeChild(tempTextarea);
    alert('Link copied to clipboard!');
}