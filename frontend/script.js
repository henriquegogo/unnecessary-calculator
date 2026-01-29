let should_clean = false

function set_num(n) {
  if (should_clean) {
    display.value = ''
    should_clean = false
  }
  display.value += n
}

function set_op(o) {
  num_a.value = display.value
  op.value = o
  should_clean = true
}

function result() {
  num_b.value = display.value
  form.submit()
}

window.onload = function() {
  if (location.search) {
    let params = new URLSearchParams(location.search)
    display.value = params.get('value')
    history.replaceState({}, null, location.href.split('?')[0])
    should_clean = true
  }
}
