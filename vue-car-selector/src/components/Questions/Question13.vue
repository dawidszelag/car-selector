<template>
  <div>
    <question-label
        number="13"
        help-text="- select one"
        question="Drivetrain?"/>
    <div class="answers-box">
      <radio-fields name="question13" keyValue="fwd" label="FRONT WHEEL DRIVE - a solid economical all-rounder"
                    @change="keyHandler"/>
      <radio-fields name="question13" keyValue="rwd" label="REAR WHEEL DRIVE - sportier feel" @change="keyHandler"/>
      <radio-fields name="question13" keyValue="awd" label="ALL-WHEEL DRIVE - great for all seasons"
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
