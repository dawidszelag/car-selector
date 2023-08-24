<template>
  <div class="content">
    <div class="box-info">
      <div class="box-info__title">
        <img :src="CarMatchText">
      </div>
      <div class="box-info__subtitle">
        <img :src="InfoText">
      </div>
    </div>
  </div>
</template>

<script setup lang="ts">
import CarMatchText from "@/assets/welcome-h.png"
import InfoText from "@/assets/welcome-tx.png"
</script>
<style lang="less" scoped>
.box-info {
  width: 95%;
  height: 100%;
  display: flex;
  flex-direction: column;
  align-items: center;
  justify-content: center;

  &__title {
    margin-bottom: 70px;
  }

  &__subtitle {
    margin: 0 50px;
  }

  img {
    max-width: 100%;
  }

}

</style>