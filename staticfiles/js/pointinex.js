function checkOnlyOne(element) {
    const checkboxes
        = document.getElementsByName("price");
    checkboxes.forEach((cb) => {
        cb.checked = false;
    });
    element.checked = true;
}
