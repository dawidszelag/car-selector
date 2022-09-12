<template>
  <div class="content">
    <div class="box-info">
      <div class="box-info__title">
        <img :src="CarMatchText">
      </div>
      <img :src="InfoText">
    </div>
  </div>
</template>

<script setup lang="ts">
import CarMatchText from "@/assets/welcome-to-carmatch.png"
import InfoText from "@/assets/welcome-text.png"
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
  img{
    max-width: 100%;
  }

}

</style>