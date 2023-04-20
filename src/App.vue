<template>
  <div style="text-align: center;font-size: 40px;margin-bottom: 50px;">“美食密码”——软壳蟹养殖与快速巡检装置</div>
  <div class="bar">
    <div id="food">料{{ food_text }}</div>
    <div id="rubbish">垃圾{{ rubbish_text }}</div>
    <div id="limit">极限时间:{{ time_left }}</div>
  </div>
  <div class="list">
    <CrabCard :func="getAll" v-for="item in timeList" :key="item" :time="item"></CrabCard>
  </div>
  <div v-if="empty" class="empty">
    没有待取的青蟹
  </div>
</template>

<script>
import CrabCard from './components/CrabCard.vue'
import { getList, getStatus } from '@/utils/serve'

export default {
  name: 'App',
  components: {
    CrabCard
  },
  data() {
    return {
      timeList: [],
      empty: false,
      time_left: "无",
      food_text: "充足",
      rubbish_text: "无需清理"
    }
  },
  methods: {
    getAll() {
      getStatus().then(
        (res) => {
          if (res.data.food == "green") {
            document.getElementById('food').setAttribute('style', 'background-color:#01b54c')
            this.food_text = "充足"
          }
          else if (res.data.food == "red") {
            document.getElementById('food').setAttribute('style', 'background-color:red')
            this.food_text = "不足"
          }
          if (res.data.rubbish == "green") {
            document.getElementById('rubbish').setAttribute('style', 'background-color:#01b54c')
            this.rubbish_text = "无需清理"
          }
          else if (res.data.rubbish == "red") {
            document.getElementById('rubbish').setAttribute('style', 'background-color:red')
            this.rubbish_text = "需要清理"
          }
          console.log(res.data)
        }
      )
      getList().then(
        (res) => {
          var timeList = []
          var list = res.data
          for (var item of list) {
            timeList.push(new Date(item))
          }
          this.timeList = timeList
          if (timeList.length == 0) {
            this.empty = true
          } else {
            this.empty = false
          }
        }
      )
      let count = () => {
        if (this.timeList.length != 0) {
          let dateDiff=1000*60*30-(new Date().getTime()-this.timeList[0].getTime())
          console.log(dateDiff)
          var minutes = parseInt(dateDiff/1000/60)
          var seconds = parseInt(dateDiff/1000- minutes*60)
          this.time_left=minutes+"分"+seconds+"秒"
        }
        else {
          this.time_left = "无"
        }
      }
      count()
      setInterval(() => {
        count()
      }, 1000)

    }
  },
  created() {
    this.getAll()
  }
}
</script>

<style>
.list {
  display: flex;
  flex-direction: column;
  align-items: center;
}

.empty {
  display: flex;
  flex-direction: column;
  align-items: center;
  margin-top: 200px;
  font-size: 50px;
}

.bar {
  width: 80%;
  position: relative;
  border-radius: 16px;
  background-color: white;
  box-shadow: 0px 5px 20px rgba(0, 0, 0, 0.1);
  height: 30px;
  margin: 0 auto;
  display: flex;
  line-height: 30px;
  justify-content: space-between;
}

#food {
  border-radius: 16px 0 0 16px;
  background-color: #01b54c;
  width: 200px;
  text-align: center;
  color: white;
}

#rubbish {
  background-color: #01b54c;
  width: 200px;
  text-align: center;
  color: white;
}

#limit {
  background-color: red;
  width: 200px;
  text-align: center;
  color: white;
  border-radius: 0 16px 16px 0;
}
</style>