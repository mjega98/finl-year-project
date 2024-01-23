window.onload = () =>{
    let now = new Date()
    let messages = document.querySelectorAll('.messages')
    const dates = document.querySelectorAll('.current-dates')

    messages.forEach((element, index) => {
        element.style.setProperty('--index', index)
        element.querySelector('i').onclick = ()=>element.remove()
        setTimeout(() => { element?.remove?.() }, 5000 + (index * 1000))
    })
    
    dates.forEach(ele => {
        ele.textContent = ele.textContent.replace(/\{time\}/g, now.getTime())
        ele.textContent = ele.textContent.replace(/\{year\}/g, now.getFullYear())
    })
}
