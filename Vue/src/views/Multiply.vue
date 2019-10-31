<template>
  <div>
    <van-nav-bar
      title="Booth算法"
    />
    <van-field
      label="乘数"
      placeholder="请输入乘数"
      v-model="multiplicand"
    />
    <van-field
      label="被乘数"
      placeholder="请输入被乘数"
      v-model="multiplier"
    />
    <van-button @click="main" class="button" color="linear-gradient(to right, #4bb0ff, #6149f6)">计算乘法补码</van-button>
    <van-field
      v-model="logCool"
      rows="3"
      autosize
      label="记录"
      type="textarea"
      maxlength="500"
      placeholder="等待运行"
      show-word-limit
    />
  </div>
</template>

<script>
import Vue from 'vue'
import { Toast, Notify } from 'vant'

Vue.use(Toast)
Vue.use(Notify)
export default {
  name: 'Multiply',
  data () {
    return {
      multiplicand: '-0.1101',
      multiplier: '-0.1011',
      A: null,
      B: null,
      opB: null,
      C: null,
      step: null,
      log: '',
      logCool: '',
      timer: null,
      logLength: 0
    }
  },
  methods: {
    main () {
      this.log = ''
      this.logCool = ''
      this.timer = null
      this.logLength = 0
      if (this.validator()) {
        Notify({ type: 'success', message: '输入验证通过' })
        this.recordLog('输入验证通过')
        this.getInitNumbers()
        let standardLength = this.B.length
        // accumulation this.A
        let result = ''
        // condition this.C
        let end = ''
        // core code
        for (let i = 0; i < this.step; i++) {
          let judgeOperate = this.C.substring(this.step - i - 1, this.step - i + 1)
          if (judgeOperate === '10') {
            // -X oppose
            result = this.binaryIntToString(this.stringToBinaryInt(this.A) + this.stringToBinaryInt(this.opB))
          } else if (judgeOperate === '01') {
            // X oppose
            result = this.binaryIntToString(this.stringToBinaryInt(this.A) + this.stringToBinaryInt(this.B))
          } else if (judgeOperate === '11' || judgeOperate === '00' || i === this.step - 1) {
            // directly right move
            // move last accumulation to first condition
            end = this.getLastChar(this.A) + end
            this.A = this.rightMove(this.A)
            continue
          }
          // format result to standardLength
          if (result.length < standardLength) {
            console.log('BEGIN=======DEBUG 1')
            console.log(result)
            let len = standardLength - result.length
            let addZero = []
            for (let i = 0; i < len; i++) {
              addZero.push('0')
            }
            let str = addZero.join('')
            result = str + result
            console.log('BEGIN=======DEBUG 1')
            console.log(result)
          }
          // remove carry
          if (result.length > standardLength) {
            console.log('BEGIN=======DEBUG 2')
            console.log(result)
            console.log(result.length)
            console.log(standardLength)
            result = result.substring(result.length - standardLength)
            console.log('BEGIN=======DEBUG 2')
            console.log(result)
          }
          // move last result to first end
          if (i !== this.step - 1) {
            end = this.getLastChar(result) + end
            this.A = this.rightMove(result)
          } else {
            this.A = result
          }
        }
        this.recordLog('[XY]补： ' + this.getXY(this.A + end))
        console.log(this.getXY(this.A + end))
      }
      this.write()
    },
    validator () {
      // re validator
      if (/^-?[01]\.[01]*$/.test(this.multiplier) && /^-?[01]\.[01]*$/.test(this.multiplicand)) {
        return true
      } else {
        Toast.fail('输入值有误' + '\n' + '请输入符合' + '\n' + '^-?[01]\\.[01]*$' + '\n' + '的初始值')
        this.recordLog('输入值有误')
        return false
      }
    },
    getInitNumbers () {
      console.log('--------begin--------')
      // A
      this.A = '0'
      // B X oppose
      this.B = this.opposeCodeX(this.multiplicand)
      this.recordLog('X补  ' + this.B)
      console.log('X补  ' + this.B)
      // opB -X oppose
      this.opB = this.opposeCodeX(-this.multiplicand)
      this.recordLog('-X补  ' + this.opB)
      console.log('-X补 ' + this.opB)
      // C Y oppose
      // add last 0
      this.C = this.opposeCodeY(this.multiplier) + '0'
      this.recordLog('Y补  ' + this.C)
      console.log('Y补  ' + this.C)
      this.step = this.C.length - 1
      this.recordLog('运算步数 ' + this.step)
      console.log('步数 ' + this.step)
    },
    opposeCodeX (val) {
      // modify split
      let splitString = ''
      // make val change to string
      let str = val + ''
      let head = str.split('.')[0]
      let end = str.split('.')[1]
      if (head === '0' || head === '-1') {
        // needn't oppose
        return '00' + splitString + end
      } else {
        return '11' + splitString + this.oppose(end)
      }
    },
    opposeCodeY (val) {
      let init = this.opposeCodeX(val)
      // remove the first one, let it be 1.1010 not 11.1010
      let removeFirst = init.substring(1)
      return removeFirst
    },
    oppose (str) {
      let chars = str.split('')
      let length = str.lastIndexOf('1')
      for (let i = 0; i < length; i++) {
        if (chars[i] === '0') {
          chars[i] = '1'
        } else {
          chars[i] = '0'
        }
      }
      // remove ','
      let end = chars.toString().replace(/,/g, '')
      return end
    },
    stringToBinaryInt (val) {
      return parseInt(val, 2)
    },
    binaryIntToString (val) {
      // 2 mean binary
      return val.toString(2)
    },
    getLastChar (str) {
      return str.substring(str.length - 1)
    },
    rightMove (result) {
      this.recordLog('计算结果：' + result)
      console.log('计算结果：' + result)
      let chars = result.split('')
      for (let i = chars.length - 1; i > 1; i--) {
        chars[i] = chars[i - 1]
      }
      let s = chars.toString().replace(/,/g, '')
      this.recordLog('右移结果：' + s)
      console.log('右移结果：' + s)
      return s
    },
    // all means this.A + end
    getXY (all) {
      let head = all.substring(0, 2)
      let end = all.substring(2)
      if (head === '00') {
        return '0.' + end
      } else {
        return '1.' + end
      }
    },
    recordLog (log) {
      this.log += log + '\n'
    },
    write () {
      this.logLength++
      if (this.logLength >= this.log.trim().split('\n').length && this.timer) {
        clearTimeout(this.timer)
      } else {
        this.logCool += this.log.trim().split('\n')[this.logLength] + '\n'
        this.timer = setTimeout(this.write, 200)
      }
    }
  }
}
</script>

<style scoped>
  .button {
    width: 90vw;
    margin: 5vw 5vw;
  }
</style>
