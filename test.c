#include <unistd.h>

int	ft_strlen(char *str)
{
	int	i;

	i = 0;
	while (str[i])
		i++;
	return i;
}

void	ft_swap(char *s1, char *s2)
{
	char tmp;

	tmp = *s1;
	*s1 = *s2;
	*s2 = tmp;
}

char	*rev_print(char *st)
{
	int st_1_len;
	int i;
	char *p;

	i = 0;
	st_1_len = ft_strlen(st) - 1;
	char str[st_1_len];

	while (i < st_1_len)
	{
		ft_swap(&str[i], &str[st_1_len]);
		i++;
		st_1_len--;
	}
	write(1, str, ft_strlen(st));
	return (str);
}

int	main(void)
{
	rev_print("hello world");// ALLOWED FUNCTIONS : WRITE
	return (0);
}
