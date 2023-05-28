function change() {
    var sec = document.getElementById('move');
    if (sec.className === 'main-container') {
        sec.className += 'respon';
    }
    else {
        sec.className = 'main-container';
    }
}