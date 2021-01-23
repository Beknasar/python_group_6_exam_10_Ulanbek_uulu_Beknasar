async function addFriend(event) {
    event.preventDefault();
    let addBtn = this;
    console.log(addBtn);
    console.log(addBtn.url)
    let url = addBtn.href;

    try {
        console.log(addBtn);
        console.log(addBtn.url)
        await makeRequest(url, 'POST');
        console.log("Добавлено в друзья")
        const container = document.getElementsByClassName('container')[0]
        let button_note = container.getElementsByClassName('addfriend')[0]
        container.before(note)
        button_note.innerHTML = `<h6 style="color: #155724">Добавлено в друзья</h6>`
        button_note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_success')
        setTimeout(() => note.remove(), 3000);

    }
    catch (error) {
        console.log(error);
    }
}

async function removeFriend(event) {
    event.preventDefault();
    let addBtn = this;
    let url = addBtn.href;

    try {
        await makeRequest(url, 'POST');
        console.log("Удалено из избранного")
        const container = document.getElementsByClassName('container')[0]
        let note = document.createElement('div')
        container.before(note)
        note.innerHTML = `<h6 style="color: #155724">Вы удалили фото из избранного</h6>`
        note.classList.add('mx-4', 'mx-4', 'px-3', 'py-2', 'note_success')
        setTimeout(() => note.remove(), 3000);
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