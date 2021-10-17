import lxml

#   div class="product-card-list"
#       div class="product-card"
#           div class="product-card__wrapper"
#               div class="product-card__img"
#                   div class="product-card__img-wrap"
#                       img src="img_url" <- tag-value
#               div class="product-card__brand"
#                   div class="product-card__price-commission"
#                       div class="price-commission"
#                           div class="price-commission__price"
#                               span class="price-commission__current-price" <- inside-value
#                               del class="price-commission__old-price" <- inside-value
#                   div class="product-card__brand-name"
#                       strong class="brand-name" <- inside-value, нужно удалить <span>/ </span>
#                       span class="goods-name" <- inside-value
#
#
#
#
#
#