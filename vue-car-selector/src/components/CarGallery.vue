<template>
  <div class="car_gallery">
    <div class="section-text-d">
      LET'S LOOK AT IT
      <div class="section-text-subtitle">GALLERY</div>
    </div>
    <div class="gallery">
      <div class="image-list">
        <div v-for="image in images" :key="image.id" class="gallery_item"
             :style="{ backgroundImage: 'url(' +  OpenAPI.BASE + image.image  + ')' }"
             style="background-position: center; background-size: cover; filter: blur(0.2px);"
             @click="currentImageIndex = images.indexOf(image)">
        </div>
      </div>
      <div class="main-image"
           @click="changeIndex(currentImageIndex); show();"
           :style="{ backgroundImage: 'url(' +  OpenAPI.BASE + currentCarImage?.image  + ')' }"
           style="background-position: center; background-size: cover;">
      </div>
      <vue-easy-lightbox
          :visible="visibleRef"
          :imgs="imgsRef"
          :index="indexRef"
          @hide="onHide"
      />
    </div>
  </div>
  <slot/>
</template>

<script setup lang="ts">
import VueEasyLightbox, {useEasyLightbox} from 'vue-easy-lightbox'
import {OpenAPI} from '../api';
import {computed, defineProps, ref} from "vue";

const props = defineProps(['images'])
const currentImageIndex = ref(0)

const currentCarImage = computed(() => {
  return props.images?.length ? props.images[currentImageIndex.value] : undefined
})

const imageList = computed(() => {
  return props.images.reduce((accumulator, currentValue) => {
    accumulator.push(OpenAPI.BASE + currentValue.image);
    return accumulator;
  }, [])
})
const {
  // methods
  show, onHide, changeIndex,
  // refs
  visibleRef, indexRef, imgsRef
} = useEasyLightbox({
  imgs: imageList.value,
})

</script>
<style lang="less" scoped>
.main-image img {
  width: 100%;
  height: auto;
}

.car_gallery img,
.car_main_img img {
  width: 100%;
  height: auto;
}

.car_gallery img {
  cursor: pointer;
}

.car_info {
  flex-basis: 70%;
}

.image-list {
  width: 25%;
  padding-right: 5px;
  max-height: 358px;
  overflow-y: auto;
  display: flex;
  flex-direction: column;
  justify-content: space-between;

  .gallery_item {
    width: 100%;
    margin-bottom: 2px;
    min-height: 118px;
    cursor: pointer;
  }
}

.main-image {
  width: 73%;
  height: 358px;
  cursor: pointer;
}

.gallery {
  display: flex;
  justify-content: space-between;
}
</style>