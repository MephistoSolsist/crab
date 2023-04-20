<template>
    <div class="card">
        <div class="text">
            {{ time_str }}
        </div>
        <div class="passed">
            已成熟 {{ time_passed }}
        </div>
        <button class="take" v-on:click="takeTheCard">
            取
        </button>
    </div>
</template>

<script>
import { takeCrab } from "@/utils/serve"
export default {
    name: 'CrabCard',
    props: {
        time: Date,
        func: {}
    },
    data() {
        return {
            time_str: "2022/08/31 10:49:41",
            time_passed: "0"
        }
    },
    methods: {
        takeTheCard() {
            takeCrab(this.time_str).then(
                (res) => {
                    console.log(res)
                    this.func()
                }
            )
        },
    },
    created() {
        this.time_str = this.time.toLocaleString()
        let count = () => {
            var dateDiff = (new Date()) - this.time
            let dayDiff = Math.floor(dateDiff / (24 * 3600 * 1000));
            let leave1 = dateDiff % (24 * 3600 * 1000)
            let hours = Math.floor(leave1 / (3600 * 1000))
            let leave2 = leave1 % (3600 * 1000)
            let minutes = Math.floor(leave2 / (60 * 1000))
            let leave3 = leave2 % (60 * 1000)
            let seconds = Math.round(leave3 / 1000)
            this.time_passed = (dayDiff ? (dayDiff + "天 ") : "") + (hours ? (hours + "小时") : "") + minutes + " 分钟" + seconds + " 秒"
        }
        count()
        setInterval(() => {
            count()
        }, 1000)
    }
}

</script>

<style scoped>
.card {
    width: 80%;
    height: 100px;
    position: relative;
    border-radius: 16px;
    background-color: white;
    box-shadow: 0px 10px 60px rgba(0, 0, 0, 0.1);
    margin-top: 8px;
    margin-bottom: 3px;
}


.passed {
    line-height: 100px;
    position: absolute;
    left: 200px;
    font-size: 17px;
}

.take {
    top: 0;
    background-color: #01b54c;
    height: 100px;
    width: 80px;
    position: absolute;
    right: 0;
    border: 0;
    border-radius: 0 16px 16px 0;
    line-height: 100px;
    text-align: center;
    color: white;
    font-size: 40px;
}

.text {
    line-height: 100px;
    position: absolute;
    left: 25px;
    font-size: 17px;
}
</style>