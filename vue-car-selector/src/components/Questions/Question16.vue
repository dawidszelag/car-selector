<template>
  <div>
    <question-label
        number="16"
        help-text="- select one"
        question="What are your plans?"/>
    <div class="answers-box">
      <radio-fields name="question16" keyValue="1" label="I want to buy new" @change="keyHandler"/>
      <radio-fields name="question16" keyValue="2" label="I want to buy used" @change="keyHandler"/>
      <radio-fields name="question16" keyValue="3" label="I am not sure if I want new or used" @change="keyHandler"/>
      <radio-fields name="question16" keyValue="4" label="Just browsing" @change="keyHandler"/>
    </div>
  </div>
</template>

<script setup>
import QuestionLabel from "../QuestionLabel";
import RadioFields from "../RadioFields";

const emit = defineEmits(['answers'])


const keyHandler = (key) => {

}

</script>
