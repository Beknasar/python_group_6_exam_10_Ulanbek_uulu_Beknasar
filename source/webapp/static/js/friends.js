async function addFriend(event) {
    event.preventDefault();
    let addBtn = event.target;
    let url = addBtn.href;

    try {
        await makeRequest(url, 'POST');
        console.log("Добавлено в друзья")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #155724">Добавлено в друзья</h6>`
        note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_success')
        setTimeout(() => note.remove(), 3000);
        location.reload()
    }
    catch (error) {
        console.log(error);
    }
}

async function removeFriend(event) {
    event.preventDefault();
    let removeBtn = event.target;
    let url = removeBtn.href;

    try {
        await makeRequest(url, 'POST');
        console.log("Удалено из друзей")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #155724">Вы удалили пользователя из списка друзей</h6>`
        note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_success')
        setTimeout(() => note.remove(), 3000);
        location.reload()
    }
    catch (error) {
        console.log(error);
    }
}

window.addEventListener('load', function() {
    const addButtons = document.getElementsByClassName('addFriend');
    const removeButtons = document.getElementsByClassName('removeFriend');

    for (let btn of addButtons) {btn.onclick = addFriend}
    for (let btn of removeButtons) {btn.onclick = removeFriend}
});