<template>
  <div class="question">
    <Question1 class="default" v-if="questionNumber===1"/>
    <Question2 class="default" v-if="questionNumber===2"/>
    <Question3 class="default" v-if="questionNumber===3"/>
    <Question4 class="default" v-if="questionNumber===4"/>
    <Question5 class="default" v-if="questionNumber===5"/>
    <Question6 class="default" v-if="questionNumber===6"/>
    <Question7 v-if="questionNumber===7"/>
    <Question8 v-if="questionNumber===8"/>
    <Question9 v-if="questionNumber===9"/>
    <Question10 v-if="questionNumber===10"/>
    <Question11 v-if="questionNumber===11"/>
    <Question12 v-if="questionNumber===12"/>
    <Question13 v-if="questionNumber===13"/>
    <Question14 v-if="questionNumber===14"/>
    <Question15 v-if="questionNumber===15"/>
    <Question16 v-if="questionNumber===16"/>
    <Question17 v-if="questionNumber===17"/>

  </div>
</template>

<script>
import Question1 from "@/components/QuestionsList/Question1";
import Question2 from "@/components/QuestionsList/Question2";
import Question3 from "@/components/QuestionsList/Question3";
import Question4 from "@/components/QuestionsList/Question4";
import Question5 from "@/components/QuestionsList/Question5";
import Question6 from "@/components/QuestionsList/Question6";
import Question7 from "@/components/QuestionsList/Question7";
import Question8 from "@/components/QuestionsList/Question8";
import Question9 from "@/components/QuestionsList/Question9";
import Question10 from "@/components/QuestionsList/Question10";
import Question11 from "@/components/QuestionsList/Question11";
import Question12 from "@/components/QuestionsList/Question12";
import Question13 from "@/components/QuestionsList/Question13";
import Question14 from "@/components/QuestionsList/Question14";
import Question15 from "@/components/QuestionsList/Question15";
import Question16 from "./QuestionsList/Question16";
import Question17 from "./QuestionsList/Question17";

export default {
  name: "Questions",
  components: {
    Question1,
    Question2,
    Question3,
    Question4,
    Question5,
    Question6,
    Question7,
    Question8,
    Question9,
    Question10,
    Question11,
    Question12,
    Question13,
    Question14,
    Question15,
    Question16,
    Question17,
  },
  props: {
    questionNumber: {
      type: Number,
    },
  },
};
</script>
<style scoped>

</style>
