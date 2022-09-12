<template>
  <div>
    <question-label
        number="1"
        help-text="- select all that apply"
        question="Who will drive the car?"/>
    <div class="answers-box">
      <checkout-field v-model="question.carForWoman" label="Female"/>
      <checkout-field v-model="question.carForMan" label="Male"/>
      <checkout-field v-model="question.preferNotToSay" label="Prefer not to say"/>
    </div>
  </div>
</template>

<script setup>
import {reactive, watch} from "vue";
import QuestionLabel from "../QuestionLabel";
import CheckoutField from "../CheckoutField";

const emit = defineEmits(['answers'])
const question = reactive({
  carForWoman: null,
  carForMan: null,
  preferNotToSay: null
})


watch(() => question.preferNotToSay, () => {
      if (question.preferNotToSay) {
        question.carForWoman = null;
        question.carForMan = null;
      }
    }
)

watch(() => [question.carForWoman, question.carForMan], () => {
      if (question.carForWoman || question.carForMan) {
        question.preferNotToSay = null;
      }
      emit('answers', {
        carForWoman: question.carForWoman,
        carForMan: question.carForMan
      })
    }
)
</script>
