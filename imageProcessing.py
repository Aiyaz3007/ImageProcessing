class CustomFunctions:
    def resizeAnnotations(self,image_dim:tuple,bbox:list,resize:tuple):
        """resize annotations
        Args:
            image_dim (tuple): image shape
            bbox (list): bbox coordinates [x,y,w,h]
            resize (tuple): resize dimension (x,y)

        Returns:
            list: [x,y,w,h]
        """
        width_ratio,height_ratio = [resize[idx]/image_dim[idx] for idx in range(len(resize))]
        return (bbox[0]*height_ratio,bbox[1]*width_ratio,bbox[2]*height_ratio,bbox[3]*width_ratio)
