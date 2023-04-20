import axios from 'axios'

let port="5050"
let api="http://127.0.0.1:"+port+"/"

export function addNow() {
    return axios({
        url: api+'add',
        method: 'get'
    })
}

export function getList() {
    return axios({
        url: api+'get',
        method: 'get'
    })
}

export function getStatus() {
    return axios({
        url: api+'status',
        method: 'get'
    })
}

export function takeCrab(date) {
    return axios({
        url: api+'take',
        method: 'post',
        data: {date}
    })
}
