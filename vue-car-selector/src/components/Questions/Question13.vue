<template>
  <div>
    <question-label
        number="13"
        help-text="- select one"
        question="What drive line would you like?"/>
    <div class="answers-box">
      <radio-fields name="question13" keyValue="fwd" label="front wheel drive - GOOD ECONOMICAL ALL ROUNDERL"
                    @change="keyHandler"/>
      <radio-fields name="question13" keyValue="rwd" label="rear wheel drive - SPORTIER FEELL" @change="keyHandler"/>
      <radio-fields name="question13" keyValue="awd" label="all-wheel drive - GREAT FOR ALL SEASONSL"
                    @change="keyHandler"/>
      <radio-fields name="question13" keyValue="0" label="unsure" @change="keyHandler"/>
      <radio-fields name="question13" keyValue="0" label="doesn’t matter" @change="keyHandler"/>
    </div>
  </div>
</template>

<script setup>
import {reactive} from "vue";
import QuestionLabel from "../QuestionLabel";
import RadioFields from "../RadioFields";

const emit = defineEmits(['answers'])

const question = reactive({
  fwd: null,
  rwd: null,
  awd: null
})

const keyHandler = (key) => {
  Object.keys(question).forEach(item => {
    if (key !== '0') {
      if (key === item) question[item] = true;
      else question[item] = null;
    } else {
      question[item] = null;
    }
  })

  emit('answers', question)
}

</script>
