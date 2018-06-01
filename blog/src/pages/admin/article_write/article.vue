<template>
    <div class="pages-write-article">
        <form class="article-form" v-on:submit.prevent="submit">
          <div class="title-input">
            <input class="form-control" type="text" name="title-input" placeholder="请输入标题" maxlength="85" v-model="title">
          </div>
          <div class="editor">
            <quill-editor v-model="content">
            </quill-editor>
          </div>
          <div class="article-type from-group">
            <label class="from-label">文章分类:</label>
            <select class="form-control" v-model="articleTypeSelect" style="display: inline-block; width:auto">
                <option v-for="item in articleType" v-bind:value="item">{{item}}</option>
            </select>
          </div>
          <div class="submit-article">
            <button type="submit" class="btn btn-primary">提交</button>
          </div>
        </form>
    </div>
</template>
<script>
  export default {
    data () {
      return {
        title:'',
        content: '',
        articleType: ['js', 'python', 'html', 'web', 'css'],
        articleTypeSelect: '',
        selected: '',
      }
    },
    mounted: function() {
      this.articleTypeSelect = this.articleType[0];
    },
    methods: {
      submit: function() {
        if(this.title.length === 0 || this.title.length === 0) {
          alert('标题或内容不能为空');
        } else {
          this.$axios.post('/article', {title: this.title, content:this.content, type: this.articleTypeSelect})
          .then((response) => {
            if(response.status === 200 && response.data.status === 'success') {
              alert("保存成功");
            } else {
              alert("保存失败");
            }
          })
          .catch((error) => {
            alert("保存失败");
          })
        }
      },
    },
  }
</script>

<style>
    .title-input input {
      width: 100%;
      margin-top: 50px;
      margin-bottom: 60px;
    }

    .quill-editor {
      height: 450px;
    }

    .article-type {
      margin-top: 100px;
      text-align: left;
    }

    .submit-article {
      margin-top: 20px;
      text-align: left;
    }
</style>